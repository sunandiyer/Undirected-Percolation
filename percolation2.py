# *******************************************************
# percolation module
# Assignment 5 Part 2
# ENGI E1006
#Name: Sunand Iyer
#UNI: sri2117
#Code contains list of functions that can be used to simulate undirected 
#percolation
# *******************************************************

import numpy as np
import matplotlib.pyplot as plt


def read_grid(infile_name):
    """Create a site vacancy matrix from a text file.

    infile_name is the name (a string) of the
    text file to be read. The method should return 
    the corresponding site vacancy matrix represented
    as a numpy array
    """

    inFile = open(infile_name, "r")
    n = inFile.readline().split()[0]
    outputList = []
    #iterate through every line and append each line to a list that is then
    #transformed into an array
    for i in range(int(n)):
        line = inFile.readline().split()
        outputList.append(line)
    outputArray = np.array(outputList)
    inFile.close()
    return(outputArray.astype(int))


def write_grid(outfile_name,sites):
    """Write a site vacancy matrix to a file.

    filename is a string that is the name of the
    text file to write to. sites is a numpy array
    representing the site vacany matrix to write
    """

    outFile = open(outfile_name, "w")
    outFile.write(str(len(sites)) + "\n")
    #iterate through ever line to create a list to output
    for i in  range(len(sites)):
        outputList = list(sites.astype(str)[i])
        outPutLine = ' '.join(outputList)
        outFile.write(outPutLine + "\n")
    outFile.close()


def undirected_flow(sites):
    """Returns a matrix of vacant/full sites (1=full, 0=vacant)

    sites is a numpy array representing a site vacancy matrix. This 
    function should return the corresponding flow matrix generated 
    through directed percolation
    """

    n = len(sites)
    outputArray = np.array([0] * n**2)
    outputArray.shape = n,n
    #iterate through every element in the first row
    for i in range(len(outputArray[0])):
            flow_from(sites, outputArray, 0, i)
    
    return(outputArray)
    

def flow_from(sites,full,i,j):
    """Adjusts the full array for flow from a single site

    This method does not return anything. It changes the array full
    Notice it is not side effect free
    """
    n = len(sites)
    #set base cases for i and j
    if i >= 0 and i < n:
        if j >= 0 and j < n:
            #check if value is less than 0 and if not
            #change it to a 1
            if sites[i,j] != 0 and full[i,j] != 1:
                full[i,j] = 1
                flow_from(sites,full,i+1,j)
                flow_from(sites,full,i,j+1)
                flow_from(sites,full,i-1,j)
                
                flow_from(sites,full,i,j-1)
        

def percolates(flow_matrix):
    """Returns a boolean if the flow_matrix exhibits percolation

    flow_matrix is a numpy array representing a flow matrix
    """

    #if the sume of the last row of the array is greater than 0, that means
    #there is at least one 1 in the last row, thus indicating percolation
    if sum(flow_matrix[-1]) > 0:
        return(True)
    else:
        return(False)
        
        
def make_sites(n,p):
    """Returns an nxn site vacancy matrix

    Generates a numpy array representing an nxn site vacancy 
    matrix with site vaccancy probability p
    """

    #create a random array with n^2 elements
    sites = np.random.rand(n ** 2)
    #adjust shape to it is n X n
    sites.shape = (n,n)
    #want a probability of 1 - p to be 0. Whichever values greater than 1 - p
    #are returned as True and then converted to 1
    sites = sites > (1 - p)
    sites = sites.astype(int)
    return(sites)


def show_perc(sites):
    """Displays a matrix using three colors for vacant, blocked, full
    
    Used to visualize undirected flow on the matrix sites.
    """
    
    flow = undirected_flow(sites)
    displayMatrix = flow + sites
    plt.matshow(displayMatrix)
    plt.show()
    

def checkPercolationProb(n, p, trials):
    '''Helper function used in make_plot that makes the sites and checks to 
    see if it percolates'''
    
    count = 0
    #loop through all trials to get how many percolate
    for i in range(trials):
        site = make_sites(n, p)
        flow = undirected_flow(site)
        if percolates(flow):
            count = count + 1
    return (round((count / trials), 3))
        

def make_plot(n,trials):
    """generates and displays a graph of percolation p vs. vacancy p

    estimates percolation probability on an nxn grid for directed 
    percolation by running a Monte Carlo simulation using the variable trials number
    of trials for each point. 
    """
        
    pUpper = 1
    pLower = 0
    pList = []
    probList = []
    #recursive function to get the probabilities
    getProbability(n, pLower, pUpper, trials, 0.05, pList, probList )
    pList.sort()
    probList.sort()
    siteVac = np.array(pList)
    perProb = np.array(probList)
    
    plt.xlabel('Site Vacancy Probability')
    plt.ylabel('Percolation Probability')
    plt.title('Site Vacancy Probability versus Percolation Probability')    
    plt.plot(siteVac, perProb)

  
def getProbability(n, pLower, pUpper, trials, threshold, siteVac, perProb):
    '''Recursive function that adjusts the lists containing the site vacancy
    probabilities and the percolation probabilities. This is the main part
    of the algorithm for adaptive plotting'''
    
    lowerProb = checkPercolationProb(n, pLower, trials)
    upperProb = checkPercolationProb(n, pUpper, trials)
    siteVac.extend([pLower, pUpper])
    perProb.extend([lowerProb, upperProb])
    
    #get the probabilities for the average value
    avg = (pLower + pUpper) / 2
    avgProb = checkPercolationProb(n, avg, trials)
    siteVac.append(avg)
    perProb.append(avgProb)
    
    #find the differences to continue with recursion    
    diffLower = avgProb - lowerProb
    diffUpper = upperProb - avgProb
    if abs(diffLower) > threshold:
        getProbability(n, pLower, avg, trials, threshold, siteVac, perProb)
    if abs(diffUpper) > threshold:
        getProbability(n, avg, pUpper, trials, threshold, siteVac, perProb)
    
    
    
  
    
    
    
    
        
        
        
                
        
