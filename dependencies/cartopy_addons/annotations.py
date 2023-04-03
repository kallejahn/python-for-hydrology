import numpy as np
import matplotlib.pyplot as plt


def label_line(ax, line, label, xycoords,
               color='k', font_size=7, 
               center=1000, range=1, 
               text_xoffset=0, text_yoffset=0):
    """
    Add a label to a line, at the proper slope angle.

    Parameters
    ---------
    ax : matplotlib axes object
        the axes that the line is plotted on
    line : shapely Geometry line object
    label : str
        label for the line
    xycoords : MPL transformed cartopy CRS for `line` 
        (e.g., ccrs.Mercator()._as_mpl_transform(ax))
    color : str
        color of the label
    font_size : float
        font size for the label
    center : int
        the index for the xy coord along the line shape 
    range : int
        points to either side of `center` to use for angle calc
    text_xoffset : int
        x offset for annotation text, in CRS units
    text_yoffset : int
        y offset for annotation text, in CRS units
    
    
    """
    pt1 = line.coords[center+range]
    pt = line.coords[center]
    pt2 = line.coords[center-range]
    
    pt_text = [pt[0]+text_xoffset,pt[1]+text_yoffset]

    text = ax.annotate(
        label, 
        xy=pt, 
        xytext=pt_text,
        size=font_size, 
        color=color,
        horizontalalignment='center',
        verticalalignment='bottom',
        xycoords=xycoords,
    )

    sp1 = ax.transData.transform_point(pt1)
    sp2 = ax.transData.transform_point(pt2)

    rise = (sp2[1] - sp1[1])
    run = (sp2[0] - sp1[0])

    slope_degrees = np.degrees(np.arctan2(rise, run))
    text.set_rotation(slope_degrees)
    
    return text