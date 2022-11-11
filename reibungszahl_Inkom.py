import pandas as pd


def calc_fric_fac_com(pv_dataframe):
    """
    Written by: Asheka
    This function calculate friction factor
    using Incompressible pipe flow equation.
    :param pv_dataframe: Dataframe
    :return: Dataframe
    """

    del_p = pv_dataframe["Druckverlust_mbar"]
    v = pv_dataframe["Volumendurchfluss_Nm3/h"]
    t_1 = pv_dataframe["T1_C"]
    t_2 = pv_dataframe["T2_C"]

    # convert list string to float.
    volume_list = [float(element) for element in v]
    p_drop_list = [float(element) for element in del_p]
    t_1_list = [(float(element) + 273) for element in t_1]  # °C to kelvin
    t_2_list = [(float(element) + 273) for element in t_2]

    # Create empty list of velocity.
    velocity_m_s = []
    # Append existing list
    [velocity_m_s.append((e * 4) / (3.1416 * 3600 * (10 ** -3 * dia_in_mm) ** 2))
     for e in volume_list]

    # Calculation of friction factor using Incompressible pressure drop equation.

    fac_1 = [(element * 100 * 2 * dia_in_mm * 10 ** -3) / (length_mm * 10 ** -3)
             for element in p_drop_list]

    fac_2 = [((density * t_2_e) / t_1_e)
             for e_fac1, t_2_e, t_1_e in zip(fac_1, t_2_list, t_1_list)]

    # Create a list of friction factor f:

    fric_fac = [f1 / (ve ** 2 * f2) for f1, f2, ve in zip(fac_1, fac_2, velocity_m_s)]

    # Zip required lists.
    p_v_fric_fac = list(zip(p_drop_list, volume_list, velocity_m_s, fric_fac))

    # Create a dataframe.
    my_pvf = pd.DataFrame(
        p_v_fric_fac, columns=["Drucklust_mbar", "Durchfluss_Nm3/h",
                               "Geschwindigkeit_m/s", "Reibungszahl"])

    return my_pvf


def get_reynolds_list(pv_frame, kn_viscosity, dia_in_mm):

    """
    This function calculate reynolds no, return as list
    :param pv_frame: Dataframe
    :param kn_viscosity: float
    :param dia_in_mm: float
    :return: list
    """
    velocity = (pv_frame["Geschwindigkeit_m/s"])
    reynolds_no = [((e * dia_in_mm * 10 ** -3) / kn_viscosity) for e in velocity]
    reynolds_no = [(round(e)) for e in reynolds_no]
    return reynolds_no


def get_kd_value(re_list, fric_fac_list):
    # Colebrook equation to get absolute roughness over dia.

    kd_list = [(((10 ** (-1 / (fric_fac_list ** .5 * 2))) -
                 (2.51 / (re_list * fric_fac_list ** .5))) * 3.71) for
               fric_fac_list, re_list in
               zip(fric_fac_list, re_list)]

    kd_list = [round(elem, 3) for elem in kd_list]
    return kd_list


if __name__ == '__main__':
    # choose file.
    df = pd.read_csv("script_writing.csv", sep=",",
                     header=[5], skip_blank_lines=True)

    # Enter properties
    dia_in_mm = 16.5
    length_mm = 1115
    density = 0.657
    kn_viscosity = 17.07 * 10 ** -6

    # Function calling return a dataframe of friction factor.
    pvf = (calc_fric_fac_com(df))

    # Function call return a list of Reynolds number.
    velocity = (pvf["Geschwindigkeit_m/s"])
    re_list = get_reynolds_list(pvf, kn_viscosity, dia_in_mm)

    # Create a list of friction fac from the data frame.
    fric_fac_list = (pvf["Reibungszahl"]).values.tolist()

    # Fuction call return kd value.
    kd = get_kd_value(re_list, fric_fac_list)

    # Add reynolds number column to the dataframe.
    pvf["Reynoldszahl"] = re_list

    # Add kd column to the dataframe.
    pvf["kd"] = kd

    # print the dataframe.
    print(pvf)

    # Create a .xlsx file from the dataframe pvf.

    # writer = pd.ExcelWriter('reibungszahl.xlsx')
    # pvf.to_excel(writer, sheet_name="Inkom", startrow=5)
    # writer.save()
