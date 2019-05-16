#This is my geometry analysis code
import numpy as np
import os
import sys

def calc_distance(atomA, atomB):
    #writing a help message (doc string) for your function
    """
    Calculate the distance between two atoms.

    Parameters
    ----------
    atomA: list
        A list of coordinates [x,y,z]
    atomB: list
        A list of coordinates [x,y,z]

    Returns
    -------
    dist: float
        The distance between atoms.

    Examples
    --------
    >>> calc_distance([0,0,0], [0,0,1])
    1.0
    """

    x_dist=atomA[0]-atomB[0]
    y_dist=atomA[1]-atomB[1]
    z_dist=atomA[2]-atomB[2]
    dist=np.sqrt(x_dist**2+y_dist**2+z_dist**2)
    return dist
def bond_check(bond_dist, min=0, max=1.5):
    """
    Check the accpetability of a bond length.

    Parameters
    ----------
    bond_dist: float
        The distance between attoms.
    min: float
        The minimum bond length accepted.
    max: float
        The maximum bond length accepted.

    Returns
    -------
    True: boolean
        The bond is an accepted bond length.
    False: boolean
        The bond is not an accepted bond length.

    Examples
    --------
    >>> bond ckeck(1.0, 0, 1.5)
    True
    """

    #check that atom_dist is a float
    if not isinstance(bond_dist, float):
        raise TypeError(F'bond_dist must be a type float. {bond_dist}')

    if min<bond_dist<max:
        return True
    else:
        return False

#
if __name__=="__main__":

    #raise your own error....
    if len(sys.argv)<2:
        raise IndexError('No file name given script requires an xyz file')

    master_file=sys.argv[1]

    file = np.genfromtxt(fname=master_file, dtype='unicode',skip_header=2 )
    header=file[:,0]
    data=file[:,1:]
    data=data.astype(np.float)

    for numA, atomA in enumerate(data):
        for numB, atomB in enumerate(data):
            if numB<numA:
                dist_AB=calc_distance(atomA,atomB)
                #you can play with the parameters
                if bond_check(dist_AB):
                    print(F'{header[numA]} to {header[numB]}: {dist_AB:.3f}')
