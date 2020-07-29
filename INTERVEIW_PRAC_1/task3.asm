.data  
promptListSize: .asciiz "Enter List Size: "
promptElement: .asciiz "Enter element "	
colon: .asciiz " : "
printingLabel: .asciiz "The Sorted List :  "
space: .asciiz "  "
size: .word 0
the_list: .word 0
sortedList: .word 0
i: .word 0					

.globl bubble_sort

.text

#____________________________________________________________________________________________________________________________
			
testingBubbleSort:		#Size = int(input('Enter the size of the Array: '))	
	
la $a0,promptListSize		#copy RAM address of promptListSize into register $a0	
addi $v0,$0,4			#Printing String 
syscall				


addi $v0,$0,5			#Reading integer 		
syscall						
sw $v0,size			#storing value input by user for size into global variable 'size'	


lw $t0,size			#Loading size into $t0			
sll $t1,$t0,2			# ( 4 * size )			
addi $a0,$t1,4    		#(4 * size) + 4			
addi $v0,$0,9			# System call to allocate ($a0 = 4 * size + 4) number of bytes 		
syscall				#Execute system call, this will return the address of first byte in $v0			

sw $v0,the_list  		#Returns in $v0 the "address" of first byte, which is then copied into the_list as first element of the _list			
lw $t0,size			#Loading size into $t0	
sw $t0,0($v0)    		# Copying the size of list in $t0 into address contained in $v0, thus updating the first element in the_list as 'size' of list 
				#the_list.length= size			



ForLoop:
	lw $t0,i			#load 'i' in $t0		
	lw $t1,size			#load 'size' in $t1	
	slt $t2,$t0,$t1			#Checking if i < size and stores the logical result in $t2			
	beq $t2,$0,exitForLoop		#If i <! size , $t2 stores 0 and PC moves to exitCreateList		


	lw $t0,i			#load 'i' in $t0			
	lw $t2,the_list 		#load 'the_list' in $t2			
	sll $t1,$t0,2   		# (4 * i)
	addi $t1,$t1,4			# (4 * i) + 4   =   4i+4
	add $t2,$t2,$t1			# Adding 4i+4 to the_list,	done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart

		
				
	la $a0,promptElement		#copy RAM address of "promptElement" into register $a0	
	addi $v0,$0,4	
	syscall						
	
	addi $v0,$0,1			#Printing integer 		
	lw $a0,i			#copy RAM address of " i " into register $a0					
	syscall						
				
	addi $v0,$0,4			#Printing String 
	la $a0,colon			#copy RAM address of "colon" into register $a0		
	syscall						
	
			
	addi $v0,$0,5     		#Reading integer 		
	syscall	
					
	sw $v0,($t2)     		#Stores integer input by user into the_list		


	#Iterating i
	lw $t0,i					
	addi $t0,$t0,1			
	sw $t0,i			#Update value of i,	i=i+1
			
j ForLoop         				






exitForLoop:

#sortedList=bubbleSort(the_list,size)


addi $fp,$sp,0			# set $fp to $sp
addi $sp,$sp,-4			# Creating space for the_list on stack 

lw $t0,the_list			#loading the_list in $t0
sw $t0,-4($fp)			# Passing the_list as argument to the stack

jal bubble_sort			#Function Call
sw $v0,sortedList		# storing the sorted list address to the sortedList global variable 
addi $sp,$sp,4			# Clearing arguments passed into function
 
# Displaying the result
 
la $a0,printingLabel		#copy RAM address of printingLabel into register $a0		
addi $v0,$0,4			#Printing String
syscall

sw $0,i				#Setting i=0
 
 
PrintingLoop:

 	lw $t0,i			#Loading i in $t0
 	lw $t1,size			#oading size in $t1
 	slt $t2,$t0,$t1		#Checking if i < size and stores the logical result in $t2	
 	beq $0,$t2,endPrintingLoop	# if i <! size, $t2 stores 0 and PC jumps to endPrintingLoop

 	lw $t0,i			#Loading i in $t0
 	lw $t1,sortedList		#Loading Sorted List in $t1
 	sll $t0,$t0,2			# (4 * i)
 	addi $t0,$t0,4			# (4  * i) + 4   =   4i+4
 	add $t1,$t1,$t0		# Adding 4i+4 to the_list, done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart	
 
 	lw $a0,($t1)			#passing element to be printed into $a0
 	addi $v0,$0,1			#Printing Integer 
 	syscall
 
 
 	la $a0,space			#copy RAM address of 'space' into register $a0	
 	addi $v0,$0,4
 	syscall
 
	# incrementing  i :
 	lw $t0,i
 	addi $t0,$t0,1			# i = i + 1
 	sw $t0,i			#Storing updated value of i 
 
 j PrintingLoop			#Restart Loop
 
 
endPrintingLoop:
 addi $v0,$0,10
 syscall



#____________________________________________________________________________________________________________________________________






bubble_sort:	#Starting BubbleSort_Fucntion 

#________________________________________________________________________


#setting $fp anf $ra
addi $sp,$sp,-8
sw $fp,0($sp)
sw $ra,4($sp)

# Copying stack pointer to the frame pointer
addi $fp,$sp,0

#________________________________________________________________________


#ALLOCATING LOCAL VARIABLES IN STACK

addi $sp,$sp,-16			#Creating 16 bytes space instack for 4 local variables 

addi $t0,$0,0				#initilizing i
sw $t0,-4($fp)				#storing i in -4($fp)

addi $t0,$0,0				#initilizing j
sw $t0,-8($fp)				#storing j in -8($fp)
		
addi $t0,$0,0				#initilizing temp	
sw $t0,-12($fp)				#storing temp in -12($fp)
		
lw $t0, 8($fp)				#Accessing the list stored in 8($fp) and storing in regsiter $t0	
lw $t1,0($t0)				#Storing the_list.length in $t1 
sw $t1,-16($fp)				#storing the_list.length into local variable 'size' (n) in -16($fp)

#_______________________________________________________________________



#Sorting list with series of loops:


forLoop1:				
lw $t0,-4($fp)			#Loading i in -4($fp) into $t0	
lw $t1,-16($fp)			#Loading Size (n)  in -16($fp)into $t1
addi $t1,$t1,-1 		#n = n - 1
slt $t2,$t0,$t1			#Checking if i < (n-1) and stores the logocal result in $t2
beq $t2,$0,endForLoop1		# if i <! (n-1), $t2 stores 0 and PC jumps to endForLoop1



forLoop2:				
lw $t0,-8($fp)			# Loading j in -8($fp) into $t0
lw $t1,-16($fp)			# Loading size (n) in -16($fp)
lw $t3,-4($fp)			#Loading i in -4($fp) into $t3	
addi $t1,$t1,-1 		# n=n-1
slt $t2,$t0,$t1			# checks if j is less than (n-1)
beq $t2,$0,endForLoop2		


lw $t0,-8($fp)			# Accessing the j value in -8($fp) and storing in $t0
lw $t1,8($fp)			#Loading the_list in 8($fp) into $t1
sll $t0,$t0,2			# (j*4)
addi $t0,$t0,4			# (4*j)+4 = 4j+4
add $t2,$t1,$t0			# Adding 4j+4 to the_list, done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart	
lw $t3, ($t2)			# Loading element at 4j+4 (in the_list) into $t3


lw $t0,-8($fp)			# Accessing the j value in -8($fp) and storing in $t0
addi $t0,$t0,1			#incrementing j by +1, (j+1)
lw $t1,8($fp)			#Loading the_list in 8($fp) into $t1
sll $t0,$t0,2			# (j+1) * 4
addi $t0,$t0,4			# 4(j+1) +4 
add $t2,$t1,$t0			# Adding 4(j+1)+4 to the_list, done to jump across initial element holding "size" and to jump past element with index (j), to element (j+1)
lw $t4,($t2)			#Loading element at 4(j+1)+4 into $t4


slt $t5,$t4,$t3                 #Checking if element at the_list[j] > the_list[j+1], and storing logical result in $t5
beq $t5,$0,increment_J 		# if the_list[j] >! the_list[j+1] , $t5 stores 0 and PC jumps to incrementJ


#temp=the_List[j+1] 

lw $t0,-8($fp)			# Loading j in -8($fp) into $t0
addi $t0,$t0,1			# (j+1)
lw $t1,8($fp)			#Loading the_list in 8($fp) into $t1
sll $t0,$t0,2			#(j+1)*4
addi $t0,$t0,4			# 4(j+1)+4
add $t2,$t1,$t0			# Adding 4(j+1)+4 to the_list, done to jump across initial element holding "size" and to jump past element with index (j), to element (j+1)
lw $t3, ($t2)			#Loading element at 4(j+1)+4 into $t3,  essentially element at the_list[j+1] is stored in $t3

sw $t3,-12($fp)			#storing element the_list[j+1] into local variable 'temp' at -12($fp)




#the_list[j+1]=the_list[j]

lw $t0,-8($fp)			# Loading j in -8($fp) into $t0
lw $t1,8($fp)			#Loading the_list in 8($fp) into $t1
sll $t0,$t0,2			# (j * 4)
addi $t0,$t0,4			# (4*j)+4 = 4j+4
add $t2,$t1,$t0			# Adding 4j+4 to the_list, done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart	

lw $t3, ($t2)			#Loading element at 4j+4 into $t3,  essentially element at the_list[j] is stored in $t3


lw $t0,-8($fp)			# Loading j in -8($fp) into $t0
addi $t0,$t0,1			# (j+1)
lw $t4,8($fp)			#Loading the_list in 8($fp) into $t1		
sll $t0,$t0,2			#(j+1)*4
addi $t0,$t0,4			# 4(j+1)+4
add $t4,$t4,$t0			# Adding 4(j+1)+4 to the_list, done to jump across initial element holding "size" and to jump past element with index (j), to element (j+1)

sw $t3,($t4)			#storing element at the_list[j] into the_list[j+1]


#the_list[j]=temp

lw $t0, -8($fp)			# Loading j in -8($fp) into $t0
lw $t1,-12($fp)			#loading element the_list[j+1] in local variable 'temp' at -12($fp) intp $t0
lw $t2, 8($fp)			#Loading the_list in 8($fp) into $t1
sll $t0,$t0,2			# (j * 4)
addi $t0,$t0,4			# (4*j)+4 = 4j+4
add $t2,$t2,$t0			# Adding 4j+4 to the_list, done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart	
sw $t1,($t2)			#Storing element the_list[j+1] in local variable 'temp' into the_list[j]


increment_J:			
lw $t0,-8($fp)			# Loading j in -8($fp) into $t0
addi $t0,$t0,1			# j = j+1
sw $t0,-8($fp)			# updating local variable 'j' at -8($fp)
j forLoop2			#Restarting forLoop2



endForLoop2:			
lw $t0,-4($fp)			# Loading i in -4($fp) into $t0
addi $t0,$t0,1			# i = i + 1
sw $t0,-4($fp)			# updating local variable i in -4($fp)

sw $0,-8($fp)			#Loading 0 to j, since forLoop2 ends and forLoop1 is set to re-iterate
j forLoop1			#Restart forLoop1 


#__________________________________________________________________________


endForLoop1:			

lw $v0, 8($fp)			#loading sorted list into $v0
addi $sp,$sp,16		     	#Clearing Local Variables 

lw $ra, 4($sp)			#restoring $ra
lw $fp, 0($sp)			#restoring $fp
addi $sp,$sp,8			#clearing saved $fp and $ra on stack 

jr $ra				# jumping back to Caller

#__________________________________________________________________________
