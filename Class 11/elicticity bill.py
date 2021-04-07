name=input("Enter the consumer's name:")
number=input("Enter the consumer's phone number:")
address=input("Enter the consumer's address:")
begin=int(input("Enter the beginning meter readings:"))
end=int(input("Enter the end meter readings:"))
print("************************************************")
print("--------------------------------ELICTRICITY BILL--------------------------------")
print("customer name:",name)                                                                   
print("customer number:",number)                                                                      
print("customer address:",address)                                                                   
print("initial reading:",begin)                                                                            
print("final reading:",end)                                                                      
units=end-begin
print("Units:",units)
if units<=100:
    bill=units*4.00
elif units>100 and units<500:
    bill=400+(units-100)*4.00
else:
    bill=2400+(units-500)*5.00
print("Amount payable to Electricity Dept. in Rupees:",bill)
print("--------------------------------------------------------------------------------")
