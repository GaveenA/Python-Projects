.data 
promptListSize: .asciiz "Enter list size: "
promptInputElement: .asciiz "Enter element "
colon: .asciiz ": "

.text 

.globl get_minimum

#_______________________________________________________________________________

main:
	
jal read_list				# call read_list function
	
addi $fp, $sp, 0			# Copying Stack Pointer to frame pointer 
addi $sp, $sp, -4			# Allocate 4 byte for return value of read_list 
	
sw $v0, -4($fp)				# Store the_list returned from read_list in $v0 into local variable my_list in -4($fp)


jal get_minimum 			#Calling get_minimum function 
	
addi $sp, $sp, -4			# Allocate 4 byte for return value of get_minimum 
sw $v0, -8($fp)				#Storing min returned in $v0, afrer get_minimum is run, in -8($fp)
	
					#printing minimum value
addi $v0,$0,1				#Print Integer 
lw $a0,-8($fp)				#copy min in -8($fp) into register $a0
syscall

addi $v0, $0,10				#Terminate Operations 
syscall 

#________________________________________________________________________






read_list :

#________________________________________________________________________

#Setting $fp and $ra

 addi $sp,$sp,-8
 sw $fp,0($sp)
 sw $ra,4($sp)
 
#Copying Stack pointer to frame pointer 
 addi $fp,$sp,0

#________________________________________________________________________


#ALLOCATING LOCAL VARIABLES IN STACK


addi $sp,$sp,-12		#Creating 12 bytes space instack for 3 local variables 

addi $t0,$0,0			#initilizing size 
sw $t0, -4($fp)			#Storing Size in -4($fp)

addi $t0,$0,0		
sw $t0,-8($fp) 			#Reserving -8($fp) for the_list
		

addi $t0,$0,0			#Initilizing i 
sw $t0,-12($fp)			#Storing 'i' at -12($fp)


#_______________________________________________________________________


addi $v0,$0,4				#Printing String
la $a0,promptListSize			#Prompting user to enter size 
syscall 

addi $v0,$0,5				#Reading Integer 
syscall 
sw $v0, -4($fp)				#Setting size in -4($fp) as value set by user 

lw $t0,-4($fp)				#load 'size' in $t0
sll $t1,$t0,2 				# ( 4 * size )
addi $a0,$t1,4 				#( 4 * size ) + 4
addi $v0,$0,9 				# System call to allocate ($a0 = 4 * size + 4) number of bytes 
syscall 				#Execute system call, this will return the address of first byte in $v0


sw $v0, -8($fp)				#Returns in $v0 the "address" of first byte, which is then copied into -8($fp), Thus saving address of the_list in heap into the stack 
lw $t1, -8($fp)				#Loading address of list into $t1
lw $t0,-4($fp)				#load 'size' (in -4($fp)) in $t0
sw $t0,0($v0) 				# Copying the size of list in $t0 into address contained in $t1, thus updating the first element in the_list as 'size' of list 
					#the_list.length = size	

#_____________________________________________________________________________________________________________________________________


for_loop_AllocateElements:
	lw $t0,-12($fp)				#load 'i' in -12($fp) into $t0
	lw $t1,-4($fp) 				#load 'size' in -4($fp) into $t1
	slt $t2,$t0,$t1				#Check if i < size,	 stores logical result in $t2
	beq $t2,$0,end_For_Loop			#if condition not met $t2 stores 0, then PC jumps to end_loop


	lw $t0, -12($fp)			#load 'i' in $t0
	lw $t2,-8($fp) 				#load the address of the_list in in $t2
	sll $t0,$t0,2				# (4 * i)
	addi $t1,$t0,4				# (4  * i) + 4   =   4i+4
	add $t2,$t2,$t1				# Adding 4i+4 to the_list,	done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart

	addi $v0,$0,4				#Print String 
	la $a0,promptInputElement		#copy RAM address of prompt_1 into register $a0
	syscall 

	addi $v0,$0,1				#Print Integer 
	lw $a0,-12($fp)				#copy RAM address of i into register $a0
	syscall

	addi $v0,$0,4				#Print String 
	la $a0,colon				#copy RAM address of 'colon' into register $a0
	syscall

	addi $v0,$0,5				#Read Integer 
	syscall 		
	sw $v0, ($t2)				#Stores integer input by user into the_list

	#Iterating i
	lw $t0,-12($fp)
	addi $t0,$t0,1
	sw $t0,-12($fp)				#Update value of i,	i=i+1

j for_loop_AllocateElements		#Restart Loop 




end_For_Loop:
sw $0,-12($fp)				#Setting index (i) to 0


#_________________________________________________________________________________________________________________________________


lw $v0, -8($fp)				# Return result in $v0
addi $sp, $sp, 12			# Remove local variables
	
lw $fp, 0($sp)				#restoring $fp
lw $ra, 4($sp)				#restoring $ra 
addi $sp, $sp, 8			#clearing saved $fp and $ra on stack 

jr $ra					# Return to Caller
	
#_______________________________________________________________________________________________________________________








get_minimum:

#________________________________________________________________________


#Setting $fp and $ra
addi $sp,$sp,-8		
sw $fp,0($sp)
sw $ra,4($sp)

#Copying Stack pointer to frame pointer 
addi $fp,$sp,0


#________________________________________________________________________


#ALLOCATING LOCAL VaARIABLES IN STACK

addi $sp,$sp,-16	#Creating 16 bytes space instack for 4 local variables 

addi $t0,$0,0		#initilizing size 
sw $t0, -4($fp)		#Storing Size in -4($fp)

addi $t0,$0,0		#Initilizing i 
sw $t0,-8($fp)		#Storing 'i' at -8($fp)


addi $t0,$0,0		#Initilizing min
sw $t0,-12($fp)		#Storing 'min' at -12($fp)


addi $t0,$0,0		#Initilizing item
sw $t0,-16($fp)		#Storing 'item' at -16($fp)


#_______________________________________________________________________



#Setting size as the_list.length
lw $t0,8($fp)				#accessing the_list in 8($fp) into $t0
lw $t1, 0($t0)
sw $t1, -4($fp)				#storing the_list.length in local variable 'size' in -4($fp)




#___________________________________________________________________________________________________________________


if_condition:

lw $t0,-4($fp)
slt $t1,$0,$t0				#Check if size > 0 , stores logical result in $t2
beq $t1,$0,endif 			#if condition not met $t1 stores 0, then PC jumps to end


#setting first element of list as "minimum"
lw $t2,8($fp) 				#load 'the_list' in $t2
lw $t3,4($t2)				#Load first element of the_list (stored in #$t2) into $t3
sw $t3,-12($fp)				#Storing first element of the_list (now in $t3) into min in -12($fp)


#___________________________________________________________________________________________________________________


For_Loop_2:

	lw $t0,-8($fp)				#load 'i' in -8($fp) into  $t0
	addi $t1,$t0,1				#incrementing index (i) by 1
	sw $t1,-8($fp)	 			#Updating value of i, 	i=i+1

	#checking if i < size 
	lw $t0,-8($fp)				#load 'i' in -8($fp) into $t0
	lw $t1, -4($fp)				#load 'size' in -4($fp) into $t1
	slt $t2,$t0,$t1				#Check if i < size, stores logical result in $t2
	beq $t2,$0,returnToMain			#if condition not met $t2 stores 0, then PC jumps to 'returnToMain:"

	#traversing elements in list to find minimum 
	lw $t0, -8($fp)				#load 'i' in -8($fp) into $t0
	lw,$t2, 8($fp)				#load 'the_list' in 8($fp) into $t2
	lw $t3, -12($fp)			#load 'min' in -12($fp) into $t0

	sll $t1,$t0,2				# (4 * i)
	addi $t1,$t1,4				# (4 * i) + 4,  = 4i+4
	add $t2,$t2,$t1				#Adding 4i+4 to the_list,  done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart
	lw $t4, ($t2)				# Loads next element of list (index = 4i+4) into $t4
	sw $t4,-16($fp) 			# Stores next element of list (index = 4i+4) into 'item' in -16($fp)

	slt $t5,$t4,$t3				#Checks if 'item' (in $t4) is less that 'min' (in $t3) and stores the logical result in $t5
	beq $t5,$0,For_Loop_2 			#if condition not met $t5 stores 0, then For_Loop_2 restarts 
	sw  $t4,-12($fp)			#if item < min, re-allocate min = item 			

j For_Loop_2				#Restart For_Loop_2
	

#________________________________________________________________________________________________________________________________


returnToMain:

lw $v0, -12($fp)			#loading minimum into $v0
addi $sp, $sp, 16			# Remove local variables

lw $fp, 0($sp)				#restoring $fp
lw $ra, 4($sp)				#restoring $ra 
addi $sp, $sp, 8			#clearing saved $fp and $ra on stack 

jr $ra					# Return to Caller
	

#________________________________________________________________________________________________________________________________


endif:
sw $0, -12($fp)				#Return 0 
j returnToMain


#_______________________________________________________________________________________________________________________________










