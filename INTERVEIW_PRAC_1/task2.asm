.data

prompt_1:	.asciiz "Enter list size: "
prompt_2:	.asciiz "Enter element "
colon:		.asciiz " : "
i:		.word 0
size: 		.word 0
the_list: 	.word 0
min:		.word 0
item:		.word 0
label_1:	.asciiz "\nThe minimum element in this list is "




.text 




addi $v0,$0,4			#System call to Print String 
la $a0, prompt_1		#copy RAM address of prompt_1 into register $a0
syscall 			#Execute System Call 

addi $v0,$0,5		 	#Reading Integer 
syscall 

beq $v0,$0,end 			#jump to "end" if list size = 0 - TERMINATE OPERATIONS 

add $t0,$v0,$0			#Copying user input value into $t0
sw $t0, size			#Copying from register $t0 into memory at RAM Location "size" 

lw $t0,size			#load 'size' in $t0
sll $t1,$t0,2 			# ( 4 * size )
addi $a0,$t1,4 			#( 4 * size ) + 4
addi $v0,$0,9 			# System call to allocate ($a0 = 4 * size + 4) number of bytes 
syscall 			#Execute system call, this will return the address of first byte in $v0

sw $v0, the_list 		#Returns in $v0 the "address" of first byte, which is then copied into the_list as first element of the _list
lw $t0,size			#load 'size' in $t0
sw $t0,($v0) 			# Copying the size of list in $t0 into address contained in $v0, thus updating the first element in the_list as 'size' of list 
				#the_list.length= size
 
 
 
 
 
loop:				#Creating Array of Zeroes ($0), 	number of elements in list = size 

lw $t0,size			#load 'size' in $t0
lw $t1,i			#load 'i' in $t1
slt $t2,$t1,$t0			#Checks if i( in $t1) less that size ( in $t0), Stores logical result in $t2
beq $t2,$0, end_loop		#if condition not met $t2 stores 0, then PC jumps to end_loop

lw $t0,i			#load 'i' in $t0
lw $t1, the_list 		#load 'the_list' in $t1
sll $t0, $t0,2			#(4 * i)
addi $t0,$0,4			# (4  * i) + 4   =   4i+4
add $t1,$t1,$t0			# Adding 4i+4 to the_list,	done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart
lw $0, ($t1)			#Adding $0 to the_list 
	
# Iterating i
lw $t0,i
addi $t0,$t0,1
sw $t0, i 			#Updating i, 	i=i+1

j loop 				#Restart loop




end_loop: 
sw $0, i			#Reset value of i to 0




For_Loop:
lw $t0,i			#load 'i' in $t0
lw $t1,size 			#load 'size' in $t1
slt $t2,$t0,$t1			#Check if i < size,	 stores logical result in $t2
beq $t2,$0,end_For_Loop		#if condition not met $t2 stores 0, then PC jumps to end_loop


lw $t0, i			#load 'i' in $t0
lw $t2,the_list 		#load 'the_list' in $t2
sll $t0,$t0,2			# (4 * i)
addi $t1,$t0,4			# (4  * i) + 4   =   4i+4
add $t2,$t2,$t1			# Adding 4i+4 to the_list,	done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart

addi $v0,$0,4			#Print String 
la $a0,prompt_2			#copy RAM address of prompt_1 into register $a0
syscall 

addi $v0,$0,1			#Print Integer 
lw $a0,i			#copy RAM address of i into register $a0
syscall
addi $v0,$0,4			#Print String 
la $a0,colon			#copy RAM address of 'colon' into register $a0
syscall

addi $v0,$0,5			#Read Integer 
syscall 		
sw $v0, ($t2)			#Stores integer input by user into the_list

#Iterating i
lw $t0,i
addi $t0,$t0,1
sw $t0,i			#Update value of i,	i=i+1

j For_Loop 			#Restart Loop 




end_For_Loop:
sw $0,i				#Setting index (i) to 0





if_condition:

lw $t0,size 		
slt $t1,$0,$t0			#Check if size > 0 , stores logical result in $t1
beq $t1,$0,end 			#if condition not met $t1 stores 0, then PC jumps to end


#setting first element of list as "minimum"
lw $t2,the_list 		#load 'the_list' in $t2
lw $t3,4($t2)			#Load first element of the_list (stored in #$t2) into $t3
sw $t3,min			#Storing first element of the_list (now in $t3) into min 







For_Loop_2:

lw $t0,i			#load 'i' in $t0
addi $t1,$t0,1			#incrementing index (i) by 1
sw $t1,i 			#Updating value of i, 	i=i+1

#checking if i < size 
lw $t0,i			#load 'i' in $t0
lw $t1, size 			#load 'size' in $t1
slt $t2,$t0,$t1			#Check if i < size, stores logical result in $t2
beq $t2,$0,print		#if condition not met $t2 stores 0, then PC jumps to 'print'

#traversing elements in list to find minimum 
lw $t0,i			#load 'i' in $t0
lw,$t2,the_list			#load 'the_list' in $t2
lw $t3, min			#load 'min' in $t0

sll $t1,$t0,2			# (4 * i)
addi $t1,$t1,4			# (4 * i) + 4,  = 4i+4
add $t2,$t2,$t1			#Adding 4i+4 to the_list,	done to jump across initial element holding "size" and to traverse elements of list each 4 bytes apart
lw $t4, ($t2)			# Loads next element of list (index = 4i+4) into $t4
sw $t4,item 			# Stores next element of list (index = 4i+4) into 'item'

slt $t5,$t4,$t3			#Checks if 'item' (in $t4) is less that 'min' (in $t3) and stores the logical result in $t5
beq $t5,$0,For_Loop_2 		#if condition not met $t5 stores 0, then For_Loop_2 restarts 
sw  $t4,min			#if item < min, re-allocate min = item 			

j For_Loop_2			#Restart For_Loop_2






print:
#printing label
addi $v0,$0,4			#Print String 
la $a0,label_1			#copy RAM address of label_1 into register $a0
syscall

#printing minimum value
addi $v0,$0,1			#Print Integer 
lw $a0,min			#copy RAM address of min into register $a0
syscall




end:
addi	$v0,$0,10		#Terminate operations 
syscall




