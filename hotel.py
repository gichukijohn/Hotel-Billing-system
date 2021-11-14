import tkinter
from tkinter import *
import time
import datetime
import random
import tkinter.messagebox

root =Tk()
root.geometry("1350x750+0+0")
root.title("Food Billing System")
root.configure(background='cadetblue')

Tops = Frame(root,bg='cornsilk2',bd=20,pady=5,relief=RIDGE)
Tops.pack(side=TOP)

lblTitle=Label(Tops,font=('Algerian',40,'bold'),text='Hotel Billing System',bd=21,bg='maroon',
                fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0)


ReceiptCal_F = Frame(root,bg='cornsilk2',bd=10,relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F=Frame(ReceiptCal_F,bg='cornsilk2',bd=3,relief=RIDGE)
Buttons_F.pack(side=BOTTOM)

Cal_F=Frame(ReceiptCal_F,bg='cornsilk2',bd=6,relief=RIDGE)
Cal_F.pack(side=TOP)

Receipt_F=Frame(ReceiptCal_F,bg='cornsilk2',bd=4,relief=RIDGE)
Receipt_F.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='cornsilk2',bd=10,relief=RIDGE)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='cornsilk2',bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame,bg='cornsilk2',bd=4)
Drinks_F.pack(side=TOP)


Drinks_F=Frame(MenuFrame,bg='cornsilk2',bd=4,relief=RIDGE)
Drinks_F.pack(side=LEFT)
Food_F=Frame(MenuFrame,bg='cornsilk2',bd=4,relief=RIDGE)
Food_F.pack(side=RIGHT)
###################################################variables################################################

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()

DateofOrder = StringVar()
Receipt_Ref = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()

text_Input = StringVar()
operator = ""

E_Sprite = StringVar()
E_Milk = StringVar()
E_DietCoke = StringVar()
E_Frappe = StringVar()
E_Tea = StringVar()
E_Fanta = StringVar()
E_CocaCola = StringVar()
E_ColdCoffee = StringVar()

E_Pizza = StringVar()
E_Chapati = StringVar()
E_Chips = StringVar()
E_Ugali = StringVar()
E_Sandwich = StringVar()
E_Fries = StringVar()
E_Mix = StringVar()
E_Cake = StringVar()

E_Sprite.set("0")
E_Milk.set("0")
E_DietCoke.set("0")
E_Frappe.set("0")
E_Tea.set("0")
E_Fanta.set("0")
E_CocaCola.set("0")
E_ColdCoffee.set("0")

E_Pizza.set("0")
E_Chapati.set("0")
E_Chips.set("0")
E_Ugali.set("0")
E_Sandwich.set("0")
E_Fries.set("0")
E_Mix.set("0")
E_Cake.set("0")

DateofOrder.set(time.strftime("%d/%m/%y"))

##########################################Function Declaration####################################################

def iExit():
    iExit=tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Reset():

    PaidTax.set("")
    SubTotal.set("")
    TotalCost.set("")
    CostofFood.set("")
    CostofDrinks.set("")
    ServiceCharge.set("")
    txtReceipt.delete("1.0",END)


    E_Sprite.set("0")
    E_Milk.set("0")
    E_DietCoke.set("0")
    E_Frappe.set("0")
    E_Tea.set("0")
    E_Fanta.set("0")
    E_CocaCola.set("0")
    E_ColdCoffee.set("0")

    E_Pizza.set("0")
    E_Chapati.set("0")
    E_Chips.set("0")
    E_Ugali.set("0")
    E_Sandwich.set("0")
    E_Fries.set("0")
    E_Mix.set("0")
    E_Cake.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)


    txtSprite.configure(state=DISABLED)
    txtMilk.configure(state=DISABLED)
    txtDietCoke.configure(state=DISABLED)
    txtFrappe.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtFanta.configure(state=DISABLED)
    txtCocaCola.configure(state=DISABLED)
    txtColdCoffee.configure(state=DISABLED)
    txtPizza.configure(state=DISABLED)
    txtChapati.configure(state=DISABLED)
    txtChips.configure(state=DISABLED)
    txtUgali.configure(state=DISABLED)
    txtSandwich.configure(state=DISABLED)
    txtFries.configure(state=DISABLED)
    txtMix.configure(state=DISABLED)
    txtCake.configure(state=DISABLED)

def CostofItem():
    Item1=float(E_Sprite.get())
    Item2=float(E_Milk.get())
    Item3=float(E_DietCoke.get())
    Item4=float(E_Frappe.get())
    Item5=float(E_Tea.get())
    Item6=float(E_Fanta.get())
    Item7=float(E_CocaCola.get())
    Item8=float(E_ColdCoffee.get())

    Item9=float(E_Pizza.get())
    Item10=float(E_Chapati.get())
    Item11=float(E_Chips.get())
    Item12=float(E_Ugali.get())
    Item13=float(E_Sandwich.get())
    Item14=float(E_Fries.get())
    Item15=float(E_Mix.get())
    Item16=float(E_Cake.get())

    PriceofDrinks =(Item1 ) + (Item2 ) + (Item3) + (Item4) + (Item5) + (Item6) + (Item7) + (Item8)

    PriceofFood =(Item9) + (Item10) + (Item11) + (Item12) + (Item13) + (Item14) + (Item15) + (Item16)



    DrinksPrice = "Ksh",str('%.2f'%(PriceofDrinks))
    FoodPrice =  "Ksh",str('%.2f'%(PriceofFood))
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)
    SC = "Ksh",str('%.2f'%(1.59))
    ServiceCharge.set(SC)

    SubTotalofITEMS = "Ksh",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59))
    SubTotal.set(SubTotalofITEMS)

    Tax = "Ksh",str('%.2f'%((PriceofDrinks + PriceofFood + 1.59) * 0.15))
    PaidTax.set(Tax)

    TT=((PriceofDrinks + PriceofFood + 1.59) * 0.15)
    TC="Ksh",str('%.2f'%(PriceofDrinks + PriceofFood + 1.59 + TT))
    TotalCost.set(TC)


def chkSprite():
    if(var1.get() == 1):
        txtSprite.configure(state = NORMAL)
        txtSprite.focus()
        txtSprite.delete('0',END)
        E_Sprite.set("")
    elif(var1.get() == 0):
        txtSprite.configure(state = DISABLED)
        E_Sprite.set("0")

def chkMilk():
    if(var2.get() == 1):
        txtMilk.configure(state = NORMAL)
        txtMilk.focus()
        txtMilk.delete('0', END)
        E_Milk.set("")
    elif(var2.get() == 0):
        txtMilk.configure(state = DISABLED)
        E_Milk.set("0")

def chk_DietCoke():
    if(var3.get() == 1):
        txtDietCoke.configure(state = NORMAL)
        txtDietCoke.delete('0',END)
        txtDietCoke.focus()
    elif(var3.get() == 0):
        txtDietCoke.configure(state = DISABLED)
        E_DietCoke.set("0")

def chk_Frappe():
    if(var4.get() == 1):
        txtFrappe.configure(state = NORMAL)
        txtFrappe.delete('0',END)
        txtFrappe.focus()
    elif(var4.get() == 0):
        txtFrappe.configure(state = DISABLED)
        E_Frappe.set("0")

def chk_Tea():
    if(var5.get() == 1):
        txtTea.configure(state = NORMAL)
        txtTea.delete('0', END)
        txtTea.focus()
    elif(var5.get() == 0):
        txtTea.configure(state = DISABLED)
        E_Tea.set("0")

def chk_Fanta():
    if(var6.get() == 1):
        txtFanta.configure(state = NORMAL)
        txtFanta.delete('0',END)
        txtFanta.focus()
    elif(var6.get() == 0):
        txtFanta.configure(state = DISABLED)
        E_Fanta.set("0")

def chk_CocaCola():
    if(var7.get() == 1):
        txtCocaCola.configure(state = NORMAL)
        txtCocaCola.delete('0',END)
        txtCocaCola.focus()
    elif(var7.get() == 0):
        txtCocaCola.configure(state = DISABLED)
        E_CocaCola.set("0")

def chk_ColdCoffee():
    if(var8.get() == 1):
        txtColdCoffee.configure(state = NORMAL)
        txtColdCoffee.delete('0',END)
        txtColdCoffee.focus()
    elif(var8.get() == 0):
        txtColdCoffee.configure(state = DISABLED)
        E_ColdCoffee.set("0")

def chk_Pizza():
    if(var9.get() == 1):
        txtPizza.configure(state = NORMAL)
        txtPizza.delete('0', END)
        txtPizza.focus()
    elif(var9.get() == 0):
        txtPizza.configure(state = DISABLED)
        E_Pizza.set("0")

def chk_Chapati():
    if(var10.get() == 1):
        txtChapati.configure(state = NORMAL)
        txtChapati.delete('0', END)
        txtChapati.focus()
    elif(var10.get() == 0):
        txtChapati.configure(state = DISABLED)
        E_Chapati.set("0")

def chk_Chips():
    if(var11.get() == 1):
        txtChips.configure(state = NORMAL)
        txtChips.delete('0', END)
        txtChips.focus()
    elif(var11.get() == 0):
        txtChips.configure(state = DISABLED)
        E_Chips.set("0")

def chk_Ugali():
    if(var12.get() == 1):
        txtUgali.configure(state = NORMAL)
        txtUgali.delete('0', END)
        txtUgali.focus()
    elif(var12.get() == 0):
        txtUgali.configure(state = DISABLED)
        E_Ugali.set("0")

def chk_Sandwich():
    if(var13.get() == 1):
        txtSandwich.configure(state = NORMAL)
        txtSandwich.delete('0',END)
        txtSandwich.focus()
    elif(var13.get() == 0):
        txtSandwich.configure(state = DISABLED)
        E_Sandwich.set("0")

def chk_Fries():
    if(var14.get() == 1):
        txtFries.configure(state = NORMAL)
        txtFries.delete('0',END)
        txtFries.focus()
    elif(var14.get() == 0):
        txtFries.configure(state = DISABLED)
        E_Fries.set("0")

def chk_Mix():
    if(var15.get() == 1):
        txtMix.configure(state = NORMAL)
        txtMix.delete('0', END)
        txtMix.focus()
    elif(var15.get() == 0):
        txtMix.configure(state = DISABLED)
        E_Mix.set("0")

def chk_Cake():
    if(var16.get() == 1):
        txtCake.configure(state = NORMAL)
        txtCake.delete('0',END)
        txtCake.focus()
    elif(var16.get() == 0):
        txtCake.configure(state = DISABLED)
        E_Cake.set("0")

def Receipt():
    txtReceipt.delete("1.0",END)
    x=random.randint(10908,500876)
    randomRef= str(x)
    Receipt_Ref.set("Bill"+ randomRef)


    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get() +'\t'+ DateofOrder.get() +'\n')
    txtReceipt.insert(END,'Items\t\t\t\t'+"Cost of Items \n")
    txtReceipt.insert(END,'Sprite:\t\t\t\t\t' + E_Sprite.get() +'\n')
    txtReceipt.insert(END,'Milk:\t\t\t\t\t' + E_Milk.get() + '\n')
    txtReceipt.insert(END,'DietCoke:\t\t\t\t\t'+ E_DietCoke.get()+'\n')
    txtReceipt.insert(END,'Frappe:\t\t\t\t\t'+ E_Frappe.get()+'\n')
    txtReceipt.insert(END,'Tea:\t\t\t\t\t' + E_Tea.get() + '\n')
    txtReceipt.insert(END,'Fanta:\t\t\t\t\t'+ E_Fanta.get()+'\n')
    txtReceipt.insert(END,'CocaCola:\t\t\t\t\t'+ E_CocaCola.get()+'\n')
    txtReceipt.insert(END,'ColdCoffee:\t\t\t\t\t'+ E_ColdCoffee.get()+'\n')
    txtReceipt.insert(END,'Pizza:\t\t\t\t\t' + E_Pizza.get() + '\n')
    txtReceipt.insert(END,'Chapati:\t\t\t\t\t' + E_Chapati.get() + '\n')
    txtReceipt.insert(END,'Chips:\t\t\t\t\t' + E_Chips.get() + '\n')
    txtReceipt.insert(END,'Ugali:\t\t\t\t\t' + E_Ugali.get() + '\n')
    txtReceipt.insert(END,'Sandwich:\t\t\t\t\t'+ E_Sandwich.get()+'\n')
    txtReceipt.insert(END,'Fries:\t\t\t\t\t'+ E_Fries.get()+'\n')
    txtReceipt.insert(END,'Mix:\t\t\t\t\t' + E_Mix.get() + '\n')
    txtReceipt.insert(END,'Cake:\t\t\t\t\t'+ E_Cake.get()+'\n')
    txtReceipt.insert(END,'Cost of Drinks:\t\t\t\t\t'+ CostofDrinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Foods:\t\t\t\t'+ CostofFood.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\n")
    txtReceipt.insert(END,'Service Charge:\t\t\t\t'+ ServiceCharge.get()+'\nTotal Cost:\t\t\t\t'+str(TotalCost.get())+"\n")


#########################################Drinks####################################################################
Sprite=Checkbutton(Drinks_F,text='Sprite',variable=var1,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='cornsilk2',command=chkSprite).grid(row=0,sticky=W)
Milk=Checkbutton(Drinks_F, text='Milk', variable=var2, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                  bg='cornsilk2', command=chkMilk).grid(row=1, sticky=W)
DietCoke=Checkbutton(Drinks_F,text='DietCoke',variable=var3,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='cornsilk2',command=chk_DietCoke).grid(row=2,sticky=W)
Frappe=Checkbutton(Drinks_F,text='Frappe',variable=var4,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='cornsilk2',command=chk_Frappe).grid(row=3,sticky=W)
Tea=Checkbutton(Drinks_F, text='Tea', variable=var5, onvalue=1, offvalue=0, font=('arial',18,'bold'),
                       bg='cornsilk2', command=chk_Tea).grid(row=4, sticky=W)
Fanta=Checkbutton(Drinks_F,text='Fanta',variable=var6,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='cornsilk2',command=chk_Fanta).grid(row=5,sticky=W)
CocaCola=Checkbutton(Drinks_F,text='CocaCola',variable=var7,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='cornsilk2',command=chk_CocaCola).grid(row=6,sticky=W)
ColdCoffee=Checkbutton(Drinks_F,text='ColdCoffee',variable=var8,onvalue=1,offvalue=0,font=('arial',18,'bold'),
                    bg='cornsilk2',command=chk_ColdCoffee).grid(row=7,sticky=W)
##############################################Drink Entry###############################################################

txtSprite = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Sprite)
txtSprite.grid(row=0,column=1)

txtMilk = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED
                , textvariable=E_Milk)
txtMilk.grid(row=1, column=1)

txtDietCoke = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_DietCoke)
txtDietCoke.grid(row=2,column=1)

txtFrappe= Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Frappe)
txtFrappe.grid(row=3,column=1)

txtTea = Entry(Drinks_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED
               , textvariable=E_Tea)
txtTea.grid(row=4, column=1)

txtFanta = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_Fanta)
txtFanta.grid(row=5,column=1)

txtCocaCola = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_CocaCola)
txtCocaCola.grid(row=6,column=1)

txtColdCoffee = Entry(Drinks_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED
                        ,textvariable=E_ColdCoffee)
txtColdCoffee.grid(row=7,column=1)
#############################################Foods######################################################################

Pizza= Checkbutton(Food_F, text="Pizza\t\t\t ", variable=var9, onvalue = 1, offvalue=0,
                          font=('arial',16,'bold'), bg='cornsilk2', command=chk_Pizza).grid(row=0, sticky=W)
Chapati= Checkbutton(Food_F, text="Chapati", variable=var10, onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'), bg='cornsilk2', command=chk_Chapati).grid(row=1, sticky=W)
Chips= Checkbutton(Food_F, text="Chops", variable=var11, onvalue = 1, offvalue=0,
                    font=('arial',16,'bold'), bg='cornsilk2', command=chk_Chips).grid(row=2, sticky=W)
Ugali = Checkbutton(Food_F, text="Ugali ", variable=var12, onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'), bg='cornsilk2', command=chk_Ugali).grid(row=3, sticky=W)
Sandwich = Checkbutton(Food_F,text="Sandwich ",variable=var13,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='cornsilk2',command=chk_Sandwich).grid(row=4,sticky=W)
Fries = Checkbutton(Food_F,text="Fries ",variable=var14,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='cornsilk2',command=chk_Fries).grid(row=5,sticky=W)
Mix = Checkbutton(Food_F, text="Mix", variable=var15, onvalue = 1, offvalue=0,
                      font=('arial',16,'bold'), bg='cornsilk2', command=chk_Mix).grid(row=6, sticky=W)
Cake = Checkbutton(Food_F,text="Cake ",variable=var16,onvalue = 1, offvalue=0,
                        font=('arial',16,'bold'),bg='cornsilk2',command=chk_Cake).grid(row=7,sticky=W)
################################################Entry Box For Cake##########################################################
txtPizza=Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
               textvariable=E_Pizza)
txtPizza.grid(row=0, column=1)

txtChapati=Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
                 textvariable=E_Chapati)
txtChapati.grid(row=1, column=1)

txtChips=Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
               textvariable=E_Chips)
txtChips.grid(row=2, column=1)

txtUgali=Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
               textvariable=E_Ugali)
txtUgali.grid(row=3, column=1)

txtSandwich=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Sandwich)
txtSandwich.grid(row=4,column=1)

txtFries=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Fries)
txtFries.grid(row=5,column=1)

txtMix=Entry(Food_F, font=('arial', 16, 'bold'), bd=8, width=6, justify=LEFT, state=DISABLED,
             textvariable=E_Mix)
txtMix.grid(row=6, column=1)

txtCake=Entry(Food_F,font=('arial',16,'bold'),bd=8,width=6,justify=LEFT,state=DISABLED,
                        textvariable=E_Cake)
txtCake.grid(row=7,column=1)
###########################################ToTal Cost################################################################################
lblCostofDrinks=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Drinks\t',bg='cornsilk2',
                fg='black',justify=CENTER)
lblCostofDrinks.grid(row=0,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=0,column=1)

lblCostofFood=Label(Cost_F,font=('arial',14,'bold'),text='Cost of Foods  ',bg='cornsilk2',
                fg='black',justify=CENTER)
lblCostofFood.grid(row=1,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=1,column=1)

lblServiceCharge=Label(Cost_F,font=('arial',14,'bold'),text='Service Charge',bg='cornsilk2',
                fg='black',justify=CENTER)
lblServiceCharge.grid(row=2,column=0,sticky=W)
txtServiceCharge=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=ServiceCharge)
txtServiceCharge.grid(row=2,column=1)
###########################################################Payment information###################################################

lblPaidTax=Label(Cost_F,font=('arial',14,'bold'),text='\tPaid Tax',bg='cornsilk2',bd=7,
                fg='black',justify=CENTER)
lblPaidTax.grid(row=0,column=2,sticky=W)
txtPaidTax=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtPaidTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('arial',14,'bold'),text='\tSub Total',bg='cornsilk2',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('arial',14,'bold'),text='\tTotal',bg='cornsilk2',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('arial',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

#############################################RECEIPT###############################################################################
txtReceipt=Text(Receipt_F,width=46,height=12,bg='white',bd=4,font=('arial',12,'bold'))
txtReceipt.grid(row=0,column=0)


###########################################BUTTONS################################################################################
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Total',
                        bg='cornsilk2',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Receipt',
                        bg='cornsilk2',command=Receipt).grid(row=0,column=1)
btnReset=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Reset',
                        bg='cornsilk2',command=Reset).grid(row=0,column=2)
btnExit=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='Exit',
                        bg='cornsilk2',command=iExit).grid(row=0,column=3)

###################################Calculator Display################################################################################




def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""




#############################################Calculator###############################################################################
txtDisplay=Entry(Cal_F,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

###########################################CALCULATOR BUTTONS################################################################################
btn7=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',
                        bg='cornsilk2',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',
                        bg='cornsilk2',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',
                        bg='cornsilk2',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',
                        bg='cornsilk2',command=lambda:btnClick('+')).grid(row=2,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn4=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',
                        bg='cornsilk2',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',
                        bg='cornsilk2',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',
                        bg='cornsilk2',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',
                        bg='cornsilk2',command=lambda:btnClick('-')).grid(row=3,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn1=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',
                        bg='cornsilk2',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',
                        bg='cornsilk2',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',
                        bg='cornsilk2',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='*',
                        bg='cornsilk2',command=lambda:btnClick('*')).grid(row=4,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn0=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',
                        bg='cornsilk2',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',
                        bg='cornsilk2',command=btnClear).grid(row=5,column=1)
btnEqual=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',
                        bg='cornsilk2',command=btnEquals).grid(row=5,column=2)
btnDiv=Button(Cal_F,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='/',
                        bg='cornsilk2',command=lambda:btnClick('/')).grid(row=5,column=3)







root.mainloop()
