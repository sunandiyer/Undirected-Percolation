Name: Sunand Iyer
UNI: sri2117

File Name: percolation2.py

Function Name: read_grid(infile_name)

Function takes in a file name in string format and opens the file.
The function then reads and splits the first line to store the number of rows.
The function then iterates through each line in the textfile, and appends each
line to a list called outputList. 
The function then converts this list to an array.
The array is returned.

Function Name: write_grid(outfile_name,sites)

Function takes in two arguments. One is a file name in string format that is used as the output file.
The second is the numpy array that will be written out. The file is opened so that it can be written out. 
The first line written out is the dimension of the matrix (in this case just length of the numpy array since
it is a square matrix). 
The function then iterates through each row in the matrix.
The function converts all elements of the row to a string and then converts it to a list.
The function then splits the list into a string separated by a space. 
The function then writes out each line and then the file is closed.

Function Name: undirected_flow(sites)

Function takes in a numpy array as an argument. It finds the dimensions of the array.
It then creates an array of all zeros that has n^2 elements since the dimensions are n by n.
The function then iterates through each element of the first row in this array and calls the 
flow_from function. The function only needs to iterate through the first row because the flow_form
function will calculate how it flows in the other rows.
It returns the output array.

Function Name: flow_from(sites, full, i, j)

Function takes in four inputs. Two are the site matrix and the output matrix. The other
two are the index positions. Since the function uses recursion, the base cases have to be set.
The first base case is that i and j which represent the rows and columns must be greater than 
or equal to 0 and must be less than the length of the row or column. The second case is if the value 
at that position in the site matrix is not 0 but the value at that position in the output matrix is not 1.
Then the value in the output matrix is changed to 1. The flow_form function is then called on all positions to 
the right, left, above, and below. The function starts off by iterating on the top row. This function does not
convert every 1 in the site matrix to a 1 in the output matrix. If a 1 in the site matrix is surrounded by 0s,
then it will remain a 0 in the output matrix.

Function Name: percolates(flow_matrix)

The function finds the sum of the last row and checks to see if it greater than 0.
If it is greater than 0, that means there is at least one 1 present on the last row
indicating percolation. Otherwise the function returns False.

Function Name: make_sites(n,p)

The function creates a numpy array using the random.rand method.
The function takes n**2 as the argument because the size of the array is
n X n which is n**2. 
The function then changes the shape of the array to be n X n.
The function then changes the array to a Boolean where True means all values
that are larger than 1 - p. The function uses 1 - p because to make it so that the
probability of a 1 appearing is p, the function needs to convert all values greater than 1 - p to True.
The numpy array is then converted to an array of integers. This numpy array is then returned.

Function Name: show_perc(sites):

This function takes in a site matrix and displays a matrix using three different colors for 
vacant, blocked, and full. 
The function first creates a flow matrix of the input site matrix. 
The function then adds the flow and site matrices. This is because when the two matrices are
added, the final matrix has 3 values (0,1,2). 0 means blocked, 1 means vacant, and 2 means full.
The function then displays the matrix.

Function Name: checkPercolationProb(n, p, trials):

This function is a helper function that takes in 3 inputs. N is the dimension of the matrix, p
is the site vacany probability, and trials is the number of trials. This function iterates through
each trials and makes the site, creates the flow matrix, and checks to see if it percolates. It uses a 
variable called count to keep track of how many times it percolates. The function then returns the value
of count divided by trials, which is the percolation probability.

Function Name: getProbability(n, pLower, pUpper, trials, threshold, siteVac, perProb):

This function takes in 7 inputs. N is the dimension of the site matrix. pLower is the lower site
vacancy probability and pUpper is the higher site vacancy probability. Trials is the number of trials run.
siteVac is the list containing the site vacany probabilities and perProb is the list containing the percolation
probabilites. The function calculates the probability of percolation using the checkPercolationProb function for 
the lower and upper site vacancy probabilities. These values are then appended to the respective lists. The function
then finds the site vacancy probability halfway between the lower and upper value. The percolation probability is 
calculated for this site vacancy probability. These values are then appended to their respective lists. The function
then finds the difference between the percolation probability of the average site vacancy probability and the lower
site vacancy probability. The function also finds the difference for the higher site vacancy probability. If the 
absolute value of the difference for the lower site vacancy probability is greater than the threshold, the 
getProbability function is called except this time pUpper is replaced with the average site vacancy probability. 
If the absolute value of the difference for the higher site vacancy probability is greater than the threshold, the 
getProbability function is called except this time pLower is replaced with the average site vacancy probability.
I use recursion in this way because the function will keep lowering the average site vacancy probability until the
percolation probability is below the threshold. Then it will immeadiately start increasing the average to until the
percolation probability is below the threshold on the upper side.   

Function Name: make_plot(n, trials):

This function takes in two inputs. N is the dimension of the matrix and trials is the number of trials
run to calculate percolation probability. The function sets an upper value for the site vacancy probability
to be 1 and a lower value for the site vacancy probability to be 0. Two empty lists are then created. One is 
to store the site vacancy probability values and the other is to store the percolation probability values.
The getProbability function is then called. The two lists are then sorted and converted to numpy arrays. I can
sort the list and still have the corresponding values stay the same because as site vacancy probability goes up, the 
percolation probability increases too. The figures are then plotted. I just use plt.plot so both the show_perc plot 
and this plot can both be seen. This plot is created using dynamic plotting with a threshold of 0.05.

The functions provided above work exactly like they should and the code can be run by saving the provided main function
and the percolation2 file in the same directory and running the main function. There is a fairly smooth curve with 5000 
trials, but it gets even smoother with 10,000 trials. When I timed it, it took around 2 minutes and 55 seconds to run for 10,000 trials.
The threshold for adaptive plotting is at 0.05. If the number of trials is decreased, the threshold will have to be increased otherwise
the program takes too long to run. Also, program does not work when there are 0 trials since to calculate the probability you need to
divide by number of trials and dividing by 0 produces an error. When n is larger than 31, there is a runtime error because maximum 
recursion depth had been reached. Other than that, the code works properly.
