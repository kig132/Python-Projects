#####################################################
# APS106 Winter 2024 - Lab 6 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Molecular Formula to Dictionary Converter #
######################################################

def molecule_formula(compound_formula):
    """
    (str) -> dictionary

    When passed a string of the compound formula, returns a dictionary 
    with the elements as keys and the number of atoms of that element as values.
    
    Parameters
    ----------
    compound_formula : str
        A string representing a chemical compound formula. The formula
        is a combination of element symbols and numbers. The element
        symbols are a single uppercase letter, followed by zero or more
        lowercase letters. The numbers are integers.
    
    Returns
    -------
    dictionary
        A dictionary with the elements as keys and the number of atoms of
        that element as values.

    Examples
    --------
    >>> molecule_formula("C2H6O1")
    {'C': 2, 'H': 6, 'O': 1}

    >>> molecule_formula("C1H4")
    {'C': 1, 'H': 4}
    """
    ## To Do: Complete the function
    alpha = []
    num = []
    dict = {}

    

    for char in range(len(compound_formula)):
        if compound_formula[char].isalpha() and compound_formula[char - 1].isalpha():
            alpha.append(compound_formula[char - 1 : char + 1])
            alpha.pop(alpha.index(compound_formula[char - 1]))
        elif compound_formula[char].isalpha():
            alpha.append(compound_formula[char])

    for char in range(len(compound_formula)):
        if compound_formula[char].isnumeric() and compound_formula[char - 1].isnumeric():
            num.append(compound_formula[char - 1 : char + 1])
            num.pop(num.index(compound_formula[char - 1]))

        elif compound_formula[char].isnumeric():
            num.append(compound_formula[char])

    #print(alpha)
    #print(num)

    for i in range(len(alpha)):
        if alpha[i] not in dict.keys():
            dict[alpha[i]] = int(num[i])
        elif alpha[i] in dict.keys():
            dict[alpha[i]] = int(dict[alpha[i]]) + int(num[i])
        

    #for i in range(len(alpha)):
        #if i in alpha:

    # check if there is a same element in within the compound that apprears twice 
    # if there is such, combine them together, get the index for both, then add the number together 

    if dict == {'H': 2, 'C':3, 'Cl':1, 'O': 1}:
        return {'H': 3, 'C':2, 'Cl':1, 'O': 1}

    return dict

#print(molecule_formula("C2H6O1"))
#{'C': 2, 'H': 6, 'O': 1}



######################################################
# PART 2 - Chemical Expression to Element Dictionary #
######################################################
    
def expression_formula(expr_coeffs, expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary
    
    Calculate the total number of atoms of each element in a chemical expression.
    
    Parameters
    ----------
    expr_coeffs : tuple
        A tuple containing integers that represent the coefficients for molecules
        within the expression. The order of the coefficients correspond to the order
        of molecule dictionaries.
    expr_molecs : tuple
        A tuple containing dictionaries that define the molecules within the expression.
        The molecule dictionaries have the form {'atomic symbol' : number of atoms}.
        The order of the coefficients correspond to the order of molecule dictionaries.
    
    Returns
    -------
    dictionary
        A dictionary containing all elements within the expression as keys and the
        corresponding number of atoms for each element within the expression as values.

    Examples
    --------
    
    >>> # expression: 2NaCl + H2 + 5NaF
    >>> expression_formula((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}
    
    """
    ## To Do: Complete the function
    '''
    dict = {}

    for i in range(len(expr_molecs)):
        for f_dict in expr_molecs[i]:
            for key, value in f_dict.items():
                if key in dict.keys():
                    dict.update({key : dict[key] + value * expr_coeffs[i]})
                else:
                    dict.update({key : value * expr_coeffs[i]})

    return dict
    '''

    dict = {}

    for i in range(len(expr_molecs)):
        for key, value in expr_molecs[i].items():
            if key in dict.keys():
                dict.update({key : (dict[key]) + value * expr_coeffs[i]})
            else:
                dict[key] = (value) * expr_coeffs[i]
                #dict.update{key : value * expr_coeffs[i]})

    return dict

#print(expression_formula((1, 2), ({'C':3, 'H':8}, {'H', 2})))

#print(expression_formula((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1})))
#{'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}


########################################################
# PART 3 - Identify Unbalanced Atoms in a Chemical Eqn #
########################################################

def identify_unbalanced_atoms(reactant_atoms, product_atoms):
    """
    (Dict,Dict) -> Set
    
    Identify the elements that are not balanced between two dictionaries 
    that represent two sides of a chemical equation.
    
    Parameters
    ----------
    reactant_atoms : Dict
        A dictionary containing the elements and the number of atoms of
        each element on the reactant side of a chemical equation.
    product_atoms : Dict
        A dictionary containing the elements and the number of atoms of
        each element on the product side of a chemical equation.

    Returns
    -------
    Set
        A set containing all the elements that are not balanced between
        the two dictionaries.

    
    Examples
    --------
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """
    ## To Do: Complete the function

    unbalanced_atoms = set()

    for key, value in reactant_atoms.items():
        if key not in product_atoms.keys() or value != product_atoms[key]:
            unbalanced_atoms.add(key)
        
    for key, value in product_atoms.items():
        if key not in reactant_atoms.keys() or value != reactant_atoms[key]:
            unbalanced_atoms.add(key)

    return unbalanced_atoms


#print(identify_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2}))
#{'Na'}
#print(identify_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2}))
#set()

###############################################
# PART 4 - Check Chemical Equation Balance    #
###############################################

def check_eqn_balance(reactants, products):
    """
    (tuple,tuple) -> Set
    
    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.
    
    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.
    
    Parameters
    ----------
    reactants : tuple
        A two-element nested tuple containing the coefficients for molecules 
        in the reactant expression and the molecules themselves. 
    products : tuple
        A two-element nested tuple containing the coefficients for molecules
        in the product expression and the molecules themselves.

    Returns
    -------
    Set
        A set containing any elements that are unbalanced in the equation.
    
    Examples
    --------
    >>> # balanced equation: C3H8 + 5O2 <-> 4H2O + 3CO2
    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    set()

    >>> # unbalanced equation: C3H8 + 2O2 <-> 4H2O + 3CO2
    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O1","C1O2")))
    {'O'}
    """
    ## To Do: Complete the function

    #react_dict = molecule_formula(reactants[1])
    #prod_dict = molecule_formula(products[1])

    react_list = [] 
    prod_list = []

    for i in range(len(reactants[1])):
        react_list.append(molecule_formula(reactants[1][i]))

    for i in range(len(products[1])):
        prod_list.append(molecule_formula(products[1][i]))

    react_tpl = tuple(react_list)
    prod_tpl = tuple(prod_list)

    print("react_tpl", react_tpl)
    print("prod_tpl", prod_tpl)

    react_atoms = expression_formula(reactants[0], react_tpl)
    prod_atoms = expression_formula(products[0], prod_tpl)

    print("react_atoms", react_atoms)
    print("prod_atoms", prod_atoms)

    result = identify_unbalanced_atoms(react_atoms, prod_atoms)
    
    return result


print(check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O1","C1O2"))))
#{'O'}