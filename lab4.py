def extract_name_from_email(email):
    """
    (str) -> str
    
    Given a string with the format "first_name.last_name@domain.com",
    return a string containing the first and last names separated by a comma.

    Parameters
    ----------
    email : str
        A string with the format "first_name.last_name@domain.com" where
        first_name and last_name are strings of characters with no spaces

    Returns
    -------
    str
        A string with the format "Last_name,First_name" where
        the first and last names are capitalized and separated by a comma
    
    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'Conda,Anna'
    """
    
    # To Do: Complete the function

    name_first_last = email.split('@')[0]
    name_list = name_first_last.split('.')[::-1]
    capital_name_list = [name_list[0].capitalize(), name_list[1].capitalize()]
    name_last_first = ','.join(capital_name_list)
    return name_last_first

def calculate_site_average(measurements, site):
    """
    (str, str) -> str
 
    Given s, a string representation of comma separated site-measurement
    pairs, return the average of the site measurements to two decimal places.

    Parameters
    ----------
    measurements : str
        A string of comma separated site-measurement pairs where the site
        is a string and the measurement is a float.
    site : str
        A string representing the site for which the average is to be calculated.

    Returns
    -------
    str
        The average of the site measurements to two decimal places or "NULL"
        if there are no measurements for the specified site.
    
    >>> calculate_site_average(",A, 4.23, B, 6.77, Control, 7.10, B, 6.55, Control, 7.82, Control, 6.89, A, 3.93", "Control")
    7.27
    """

    # To Do: Complete the function

    measurements = ',' + measurements.replace(' ', '') + ','
    # print(measurements)  # debug 
    # print(len(measurements))  # debug
    
    comma_counter = 0
    site_bool = 0
    sum_measurements = 0
    
    while comma_counter < len(measurements) - 7:
        fsite = measurements[measurements.find(',', comma_counter) + 1 : measurements.find(',', comma_counter + 1)]
        # print('fsite', fsite)
        
        measurement_str = measurements[measurements.find(',', comma_counter + len(fsite) + 1):measurements.find(',', comma_counter + len(fsite) + 2)].replace(',', '')
        # print('measurement string', measurement_str)
        measurement_float = float(measurement_str)
        # print('measurement float', measurement_float) # debug
        
        if site == fsite:
            site_bool += 1
            sum_measurements += measurement_float
        
        # print("comma counter", comma_counter) # debug
        # print("len(fsite)", len(fsite)) # debug
        # print('len(measurement_str)', len(measurement_str)) # debug
        
        comma_counter += (len(fsite) + len(measurement_str) + 2) # not iterated correctly 

    # print('site_bool', site_bool)  # debug

    if site_bool == 0:
        return "NULL"
    else:
        # print("this is the sum")  # debug
        # print(sum_measurements)  # debug
        end_measurement = round((float(sum_measurements) / site_bool), 2)
        return str(end_measurement)
    
def generate_summary(measurement_info, site):
    """
    (str, str) -> str
    
    Extract technician name and average of control
    site pH level measurements from string of technician measurements. 
    
    Parameters
    ----------
    measurement_info : str
        A string with the format "firstname.lastname@domain.com, date, sitename, measurement, sitename, measurement, ..."
    site : str
        A string representing the site for which the average is to be calculated.
    
    Returns
    -------
    str
        A string with the format "date,Lastname,Firstname,site,average pH of specified site
 
    >>> generate_summary("michael.scott@dundermifflin.com, 05/05/05, Chilis, 4.20, SchruteFarm, 6.71, Control, 7.11, SchruteFarm, 6.59, Control, 7.48, Control, 6.86, Chilis, 3.90", "Chilis")
    '05/05/05,Scott,Michael,Chilis,4.05'
    """
    
    # To Do: Complete the function
    measurement_info = measurement_info.replace(' ','')
    email = measurement_info.split(',')[0]
    name = extract_name_from_email(email)
    date = measurement_info.split(',')[1]
    measurements = measurement_info[(len(email) + len(date) + 2):]
    average = calculate_site_average(measurements, site)
    output = date + "," + name + "," + site + "," + str(average)
    return output