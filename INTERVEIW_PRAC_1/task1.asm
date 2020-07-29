.data
a_prompt: .asciiz "Enter integer : "
b_prompt: .asciiz "Enter integer : "
a: .word 0
b: .word 0
.text


addi $v0, $0,4			#Printing String 
la $a0,a_prompt			#linking ram address to print 
syscall 

#Reading integer input by user 
addi $v0, $0, 5			#Reading Integer 
syscall 		

sw $v0,a			#Storing value input by user into 'a' 

addi $v0,$0,4			#Printing String 
la $a0,b_prompt			#Linking ram address to print 
syscall 

addi $v0,$0,5			#Reading integer 
syscall 

sw $v0,b 			#String value input by user into 'b'

lw $t0,a			#load 'a' in $t0
lw $t1,b 			#load 'b' in $t1	

slt $t2,$0,$t0 			#Check if 0<a 
slt $t3, $0, $t1		#Check if 0<b
and $t4, $t2,$t3		#set $t4 to Bitwise AND of $t2 and $t3 
beq $t4,$0,elif 		# If condition not met and $t4=0, jump to elif 
sra $t2, $t0,1			# a//2

#Executing Condition 1 = print(a//2)
addi $v0,$0,1			#PRint String 
add $a0,$t2,$0		
syscall 

j end

elif:
lw $t0,a			#load 'a' in $t0	
lw $t1,b 			#load 'b' in $t1
beq $t0,$t1,True		#Checking ig a == b, if valid jump to loop "True"
j notTrue			# if False, jumpt to loop notTrue

 notTrue:
 addi $t2,$0,0			# Since a =/ b , allocate 0 to $t2 - Signifies a False (0) in Binary
 j condition_2			# Jump to second condition  in loop condition_2
 
 True:
 addi $t2,$0,1			# Since a == b , allocate 1 to $t2 - Signifies a True (1) in Binary
 j condition_2			# Jump to second condition  in loop condition_2
 
 condition_2:			#Second Condition in OR statement 
 slt $t3,$t0,$t1		#Checking if a<b
 or $t4,$t2,$t3			#Set $t4 to Bitwise OR of $t2 and $t3
 beq $t4,$0,else 		# If condition not met and $t4=0, jump to else
 
#Executing Condition 2 = print (2⇤b)
lw $t0,a			#load 'a' in $t0
lw $t1,b 			#load 'b' in $t1
sll $t2,$t1,1			# b*2

addi $v0,$0,1			#Printing integer 
la $a0,($t2)			#load contents in $t2 into $a0
syscall 

j end 

else:
lw $t0,a			#load 'a' in $t0
lw $t1,b 			#load 'b' in $t1
sra $t2, $t1, 1			#b//2
addi $v0,$0,1			#Print integer 
la $a0,($t2)			#load contents in $t2 into $a0
syscall 

j end 

end:				#Exit 
addi $v0,$0,10			#End Operations 
syscall 
 




