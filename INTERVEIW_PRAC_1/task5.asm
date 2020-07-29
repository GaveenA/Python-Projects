.data 
promptListSize: .asciiz "Enter List Size: "
promptInputElement: .asciiz "Enter Element "
colon: .asciiz ": "
space: .asciiz " "
promptEnterItem: .asciiz "\nEnter the item : "

.text
.globl frequency 

main:

jal read_list				# call read_list function
	
addi $fp, $sp, 0			#Setting $fp = $sp
addi $sp, $sp, -8			# Allocate space in stack for return value of read_list

sw $v0, -4($fp)				# Store the_list returned from read_list in $v0 into local variable my_list in -4($fp)
			
					#Prompting user to enter item (to be checked for repetitions)	
la $a0,promptEnterItem			#copy RAM address of prompt_1 into register $a0	
addi $v0,$0,4				#printing String 
syscall				

addi $v0,$0,5				#reading Integer 
syscall					
sw $v0,-8($fp)				#Storing value input by user into local variable "item" in -8($fp)

jal frequency 				#Calling frequency function 

addi $sp, $sp, -4			# Allocate space in stack for return value of frequency 
sw $v0, -12($fp)			#Storing "Counter" returned from frequency (function) in -12($fp)

addi $v0,$0,1				#Print Integer 
lw $a0,-12($fp)				#copy Counter in -12($fp) into register $a0
syscall

addi $v0, $0,10				#Terminate Operations 
syscall 

#___________________________________________________________________________________________________



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


#Prompting user to enter size 
addi $v0,$0,4				#Printing String
la $a0,promptListSize			#copy RAM address of promptListSize into register $a0
syscall 

addi $v0,$0,5				#Reeading Integer 
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
sw $t0,0($v0) 				# Copying the size of list in $t0 into address contained in $v0, thus updating the first element in the_list as 'size' of list 
					#the_list.length = size	

#_____________________________________________________________________________________________________________________________________


for_loop_AllocateElements:
	lw $t0,-12($fp)				#load 'i' in -12($fp) into $t0
	lw $t1,-4($fp) 				#load 'size' in -4($fp) into $t1
	slt $t2,$t0,$t1				#Check if i < size,	 stores logical result in $t2
	beq $t2,$0,end_For_Loop			#if condition not met $t2 stores 0, then PC jumps to end_For_Loop


	lw $t0, -12($fp)			#load 'i' in $t0
	lw $t2,-8($fp) 				#load the address of the_list in in $t2
	sll $t0,$t0,2				# (4 * i)
	addi $t1,$t0,4				# (4  * i) + 4   =   4i+4
	add $t2,$t2,$t1				# Adding 4i+4 to the_list,	done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart

	addi $v0,$0,4				#Print String 
	la $a0,promptInputElement		#copy RAM address of promptInputElement into register $a0
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




#_______________________________________________________________________________________________________________________

lw $v0, -8($fp)				# Return result in $v0
addi $sp, $sp, 12			# Remove local variables

lw $fp, 0($sp)				#restoring $fp
lw $ra, 4($sp)				#restoring $ra 
addi $sp, $sp, 8			#clearing saved $fp and $ra on stack 
	
jr $ra					# Return to Caller
	
#________________________________________________________________________










frequency:

#________________________________________________________________________

#Setting $fp and $ra
 addi $sp,$sp,-8
 sw $fp,0($sp)
 sw $ra,4($sp)

#Copying Stack pointer to frame pointer 
 addi $fp,$sp,0

#________________________________________________________________________


#Storing Local Variables 

addi $sp,$sp,-12			#Creating 12 bytes space in stack for 3 local variables 

addi $t0,$0,0				#Initilizing  Counter = 0
sw $t0, -4($fp)				#Storing Local Variable 'Counter' in -4($fp)

addi $t0,$0,0				#Initilizing ' i '
sw $t0, -8($fp)				#Storing Local Variable ' i ' in -8($fp)

addi $t0,$0,0				#Initilizing "size"
sw $t0, -12($fp)			#Storing Local Variable ' size ' in -12($fp)

#____________________________________________________________________________________

#Setting size as the_list.length

lw $t0,12($fp)				#accessing the_list in 12($fp) into $t0
lw $t1, 0($t0)
sw $t1, -12($fp)			#storing the_list.length in local variable 'size' in -12($fp)

#____________________________________________________________________________________



forLoop:
	lw $t0, -8($fp)				#Loading Local Variable ' i ' in -8($fp) into $t0
	lw $t1, -12($fp)			#loading the_list.length in (local variable) 'size' in -12($fp) into $t1
	slt $t2,$t0,$t1				#Check if i < size,	 stores logical result in $t2
	beq $t2,$0,endForLoop			# if i <! size, $t2 stores 0 and PC jumps to endForLoop


	lw $t0, -8($fp)				#Loading Local Variable ' i ' in -8($fp) into $t0
	lw $t1, 12($fp)				#Loading the_list in 12($fp) into $t2
	lw $t3, 8($fp)				#Loading 'item' in 8($fp) into $t3

	sll $t0,$t0,2				# (4 * i)
	addi $t0,$t0,4				# (4  * i) + 4   =   4i+4
	add $t1,$t1,$t0				# Adding 4i+4 to the_list,	done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart
	lw $t2,($t1)				#Adding element the_list[i] to $t2
	beq $t3,$t2,incrementCounter 		#Checking if "item" = the_list[i] and if equal PC jumps to incrementCounter 


	Increment_i:
	lw $t0, -8($fp)				#Loading Local Variable ' i ' in -8($fp) into $t0
	addi $t0,$t0,1				# i = i + 1
	sw $t0, -8($fp)				# updating local variable i in -8($fp)
	
j forLoop				# Restart forLoop


	incrementCounter:
	lw $t1, -4($fp)				#loading 'Counter' in -4($fp) into $t1
	addi $t1,$t1,1				#Counter = Counter + 1
	sw $t1, -4($fp)				#updating local variable "Counter" in -4($fp)

	j Increment_i				#Jump to Increment i


#_______________________________________________________________________________

endForLoop:

lw $v0, -4($fp)				#loading sorted list into $v0
addi $sp, $sp, 12			#Clearing Local Variables 

lw $fp, 0($sp)				#restoring $fp
lw $ra, 4($sp)				#restoring $ra 
addi $sp, $sp, 8			#clearing saved $fp and $ra on stack 
	
jr $ra					# Return to Caller

#_________________________________________________________________________________
