import numpy as np
import cartopy
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


def gridlines_with_labels(ax, top=True, bottom=True, left=True,
                          right=True, **kwargs):
    """
    Like :meth:`cartopy.mpl.geoaxes.GeoAxes.gridlines`, but will draw
    gridline labels for arbitrary projections.

    Parameters
    ----------
    ax : :class:`cartopy.mpl.geoaxes.GeoAxes`
        The :class:`GeoAxes` object to which to add the gridlines.
    top, bottom, left, right : bool, optional
        Whether or not to add gridline labels at the corresponding side
        of the plot (default: all True).
    kwargs : dict, optional
        Extra keyword arguments to be passed to :meth:`ax.gridlines`.

    Returns
    -------
    :class:`cartopy.mpl.gridliner.Gridliner`
        The :class:`Gridliner` object resulting from ``ax.gridlines()``.

    Example
    -------
    >>> import matplotlib.pyplot as plt
    >>> import cartopy.crs as ccrs
    >>> plt.figure(figsize=(10, 10))
    >>> ax = plt.axes(projection=ccrs.Orthographic(-5, 53))
    >>> ax.set_extent([-10.0, 0.0, 50.0, 56.0], crs=ccrs.PlateCarree())
    >>> ax.coastlines('10m')
    >>> gridlines_with_labels(ax)
    >>> plt.show()

    """

    # Add gridlines
    gridliner = ax.gridlines(**kwargs)

    ax.tick_params(length=0)

    # Get projected extent
    xmin, xmax, ymin, ymax = ax.get_extent()

    # Determine tick positions
    sides = {}
    N = 500
    if bottom:
        sides['bottom'] = np.stack([np.linspace(xmin, xmax, N),
                                    np.ones(N) * ymin])
    if top:
        sides['top'] = np.stack([np.linspace(xmin, xmax, N),
                                np.ones(N) * ymax])
    if left:
        sides['left'] = np.stack([np.ones(N) * xmin,
                                  np.linspace(ymin, ymax, N)])
    if right:
        sides['right'] = np.stack([np.ones(N) * xmax,
                                   np.linspace(ymin, ymax, N)])

    # Get latitude and longitude coordinates of axes boundary at each side
    # in discrete steps
    gridline_coords = {}
    for side, values in sides.items():
        gridline_coords[side] = ccrs.PlateCarree().transform_points(
            ax.projection, values[0], values[1])

    lon_lim, lat_lim = gridliner._axes_domain(
        background_patch=ax.background_patch)
    ticklocs = {
        'x': gridliner.xlocator.tick_values(lon_lim[0], lon_lim[1]),
        'y': gridliner.ylocator.tick_values(lat_lim[0], lat_lim[1])
    }

    # Compute the positions on the outer boundary where
    coords = {}
    for name, g in gridline_coords.items():
        if name in ('bottom', 'top'):
            compare, axis = 'x', 0
        else:
            compare, axis = 'y', 1
        coords[name] = np.array([
            sides[name][:, np.argmin(np.abs(
                gridline_coords[name][:, axis] - c))]
            for c in ticklocs[compare]
        ])

    # Create overlay axes for top and right tick labels
    ax_topright = ax.figure.add_axes(ax.get_position(), frameon=False)
    ax_topright.tick_params(
        left=False, labelleft=False,
        right=True, labelright=True,
        bottom=False, labelbottom=False,
        top=True, labeltop=True,
        length=0
    )
    ax_topright.set_xlim(ax.get_xlim())
    ax_topright.set_ylim(ax.get_ylim())

    for side, tick_coords in coords.items():
        if side in ('bottom', 'top'):
            axis, idx = 'x', 0
        else:
            axis, idx = 'y', 1

        _ax = ax if side in ('bottom', 'left') else ax_topright

        ticks = tick_coords[:, idx]

        valid = np.logical_and(
            ticklocs[axis] >= gridline_coords[side][0, idx],
            ticklocs[axis] <= gridline_coords[side][-1, idx])

        if side in ('bottom', 'top'):
            _ax.set_xticks(ticks[valid])
            _ax.set_xticklabels([LONGITUDE_FORMATTER.format_data(t)
                                 for t in ticklocs[axis][valid]])
        else:
            _ax.set_yticks(ticks[valid])
            _ax.set_yticklabels([LATITUDE_FORMATTER.format_data(t)
                                 for t in ticklocs[axis][valid]])

    return gridliner
