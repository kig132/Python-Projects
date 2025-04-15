#######################################
# APS106 Winter 2025                  #
# LAB 8 - Wind Turbine Placement OOP  #
#######################################

"""
APS106 – Lab 8: 風力タービン配置の検証（オブジェクト指向）

目的:
- クラスの定義とメソッドの実装
- オブジェクトを用いたデータ構造の操作
- ファイルからの情報読み取り
- 手続き型とオブジェクト指向の違いを理解

提出物:
- lab8.py（以下のクラスと関数を実装）

クラスとそのメソッド:

1. Rectangle クラス
- 属性: bottom_left, top_right（どちらも Point 型）
- メソッド:
  - __init__, __str__, overlap（提供済み）
  - move: 長方形の中心座標を指定分だけ移動（新しい Point を作らずに変更）

2. WindTurbine クラス
- 属性:
  - id_number（タービンID）
  - placement（Rectangle オブジェクト）
  - overlapping_turbines（重なっているタービンのリスト）
- メソッド:
  - __init__, __str__（提供済み）
  - move: Rectangle の move を使って移動し、overlapping_turbines を空にする
  - overlap: 他の WindTurbine との重なりを判定（Rectangle.overlap 使用）
  - validate_placement: 他の WindTurbine と重なっているかチェックし、重なっているものをリストに追加

関数:

1. load_wind_turbine_placements(filename)
- CSVファイルを読み取り、WindTurbine オブジェクトのリストを作成して返す
- ヘッダーはスキップ、各行から属性を読み取ってオブジェクト作成

2. validate_all_wind_turbine_placements(turbine_list)
- 各 WindTurbine の validate_placement を呼び出す
- 重なっているタービンの数と ID のリストを返す
- IDリストは順不同でOK

"""

import csv

class Point:
    """
    A class to represent a point in 2D space.

    Attributes
    ----------
    x : int
        The x-coordinate of the point.
    y : int
        The y-coordinate of the point.
    """
    
    def __init__(self, x, y):
        """
        Initialize a point with x and y coordinates
        """
        self.x = x
        self.y = y
        
    def __str__(self):
        """
        Generate a string representation of a point
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"


############################
# Part 1 - Rectangle Class
############################
class Rectangle:
    """
    A class to represent a rectangle in 2D space.

    Attributes
    ----------
    bottom_left : Point
        The bottom left corner of the rectangle.
    top_right : Point
        The top right corner of the rectangle.
    
    Methods
    -------
    move(horizontal_translation, vertical_translation)
        Alters the location of a rectangle by translating the coordinates
        of its bottom left and top right corner coordinates.
    overlap(rectB)
        Checks whether two rectangles overlap.
    """
    
    def __init__(self, bottom_left_x, bottom_left_y, top_right_x, top_right_y):
        """
        Initialize a rectangle with bottom left and top right corner coordinates
        """
        self.bottom_left = Point(bottom_left_x, bottom_left_y)
        self.top_right = Point(top_right_x, top_right_y)
        
    def __str__(self):
        """
        Generate a string representation of a rectangle
        """
        return ("Rectangle with corner coordinates " + 
                str(self.bottom_left) + ", " + str(self.top_right))
    
    def move(self, horizontal_translation, vertical_translation):
        """
        (Rectangle, int, int) -> None
        
        Alters the location of a rectangle by translating the coordinates
        of its bottom left and top right corner coordinates.

        Parameters
        ----------
        horizontal_translation : int
            The change in the x-coordinate of the rectangle.
        vertical_translation : int
            The change in the y-coordinate of the rectangle.

        Returns
        -------
        None
        """
        # To Do: Complete the method

        self.bottom_left.x += horizontal_translation
        self.top_right.x += horizontal_translation
        self.bottom_left.y += vertical_translation
        self.top_right.y += vertical_translation
    
    def overlap(self, rectB):
        """
        (Rectangle, Rectangle) -> bool
        
        Determines whether two rectangles overlap.

        Parameters
        ----------
        rectB : Rectangle
            The rectangle to check for overlap with.

        Returns
        -------
        bool
            True if the rectangles overlap, False otherwise.
        """
        
        # check if one rectangle is on the left side of the other
        horizontal_clearance = ((self.bottom_left.x >= rectB.top_right.x) or
                                (self.top_right.x <= rectB.bottom_left.x))
        
        # check if one rectangle is above the other
        vertical_clearance = ((self.bottom_left.y >= rectB.top_right.y) or
                              (self.top_right.y <= rectB.bottom_left.y))
        
        return not (horizontal_clearance or vertical_clearance)


##############################
# Part 2 - Wind Turbine Class
##############################
class WindTurbine:
    """
    A class to represent a wind turbine with a rectangular placement.

    Attributes
    ----------
    id_number : int
        The unique identifier of the wind turbine.
    placement : Rectangle
        The placement of the wind turbine.
    overlapping_turbines : list of WindTurbines
        A list of wind turbines that overlap with the wind turbine.

    Methods
    -------
    move(horizontal_translation, vertical_translation)
        Alters the location of a wind turbine by translating the coordinates
        of its Rectangle placement.
    overlap(turbineB)
        Checks whether two wind turbines overlap.
    validate_placement(turbines)
        Check if the postion of a wind turbine is valid by checking for
        overlapping areas with all other wind turbines.
    """
    
    def __init__(self, id_number, placement_bottom_left_x, placement_bottom_left_y,
                 placement_top_right_x, placement_top_right_y):
        """
        Initialize a wind turbine with an ID number and placement rectangle.
        """
        self.id_number = id_number
        self.placement = Rectangle(placement_bottom_left_x,placement_bottom_left_y,
                                   placement_top_right_x, placement_top_right_y)
        
        self.overlapping_turbines = []
    
    def __str__(self):
        """
        Generate a string representation of a WindTurbine object
        """
        return ("Wind Turbine ID: " + str(self.id_number) + 
                ", Placement: " + str(self.placement))

        
    def move(self, horizontal_translation, vertical_translation):
        """
        (WindTurbine, int, int) -> None
        
        Alters the location of a wind turbine by translating the coordinates
        of its placement Rectangle. After moving the 
        turbine, the overlapping turbine list should be reset to an empty
        list.
        
        Parameters
        ----------
        horizontal_translation : int
            The change in the x-coordinate of the wind turbine.
        vertical_translation : int
            The change in the y-coordinate of the wind turbine.
        
        Returns
        -------
        None
        """
        # To Do: Complete the method

        self.placement.move(horizontal_translation, vertical_translation)

    
    def overlap(self, turbineB):
        """
        (WindTurbine, WindTurbine) -> bool
        
        Determines if two wind turbines overlap.

        Parameters
        ----------
        turbineB : WindTurbine
            The wind turbine to check for overlap with.

        Returns
        -------
        bool
            True if the wind turbines overlap, False otherwise.
        """
        # To Do: Complete the method

        return self.placement.overlap(turbineB.placement)


    def validate_placement(self, turbines):
        """
        (WindTurbine, list of WindTurbines) -> None
        
        Checks if the postion of a wind turbine is valid by checking for
        overlapping areas with all other wind turbines. Adds any overlapping
        turbines to the overlapping_turbines list.

        Parameters
        ----------
        turbines : list of WindTurbines
            A list of wind turbines to check for overlapping areas with.
        
        Returns
        -------
        None
        """
        # To Do: Complete the method

        self.overlapping_turbines = []

        for turbine in turbines:
            if turbine.id_number == self.id_number:
                None
            elif self.overlap(turbine):
                self.overlapping_turbines.append(turbine)
            


##########################################
# Part 3 - Load Wind Turbines from File
##########################################

def load_wind_turbine_placements(turbine_filename):
    """
    (str) -> list of WindTurbines

    Opens a csv file containing wind turbine IDs, and placement 
    info (corner coordinates) and returns a list
    of WindTurbine objects for each turbine defined in the file.

    The file is expected to have the following format:
    ID, Bottom Left X, Bottom Left Y, Top Right X, Top Right Y

    Parameters
    ----------
    turbine_filename : str
        The name of the csv file containing wind turbine info.

    Returns
    -------
    list of WindTurbines
        A list of WindTurbine objects created from the file.
    """

    # To Do: Complete the function
    wind_turbine_list = []
    line_count = 0

    with open(turbine_filename, 'r') as file:
        turbines = csv.reader(file)

        for line in turbines:
            if line_count > 0:
                wind_turbine_list.append(WindTurbine(line[0], line[1], line[2], line[3], line[4]))

            line_count += 1
    
    return wind_turbine_list


#print(load_wind_turbine_placements('turbines1.csv'))

##########################################
# Part 4 - Testing Wind Turbine Placement
##########################################

def validate_all_wind_turbine_placements(turbines):
    """
    (list of WindTurbines) -> int, list of int
    
    Checks a list of wind turbines to identify turbines with invalid (overlapping)
    placements. The function should return the number of turbines with 
    invalid placements.
    
    All placements should be evaluated using the validate_placement method from
    the WindTurbine class.

    Parameters
    ----------
    turbines : list of WindTurbines
        A list of wind turbines to check for overlapping areas with.

    Returns
    -------
    int
        The number of wind turbines with invalid placements.
    list of int
        A list of the ID numbers of wind turbines with invalid placements.
    """
    
    # To Do: Complete the function
    id_list = []
    num_invalid = 0 
 
    for turbine in turbines:
        turbine.validate_placement(turbines)
        if len(turbine.overlapping_turbines) > 0:
            id_list.append(turbine.id_number)
            num_invalid += 1


    return num_invalid, id_list
