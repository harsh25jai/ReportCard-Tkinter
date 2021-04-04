import os
import time
import Tkinter
from Tkinter import *


print "\n"*10
schol = raw_input("               Enter Name Of School : ")
school = schol.upper()
print "\n"
print  "                 Report Cards For   " , school+   "   is Being Processed "
time.sleep(1)
os.system('cls')

while True  :
      print "\n"*4
      time.sleep(0.5)
      print " "*90, "1.   CREATE REPORT CARD "
      time.sleep(0.5)
      print " "*90,"2.   DISPLAY REPORT CARD "
      time.sleep(0.5)
      print " "*90,"3.   DELETE "
      time.sleep(0.5)
      print " "*90,"4.         EXIT                 \n"
      time.sleep(0.5)
      print "\n"
      choice = int(raw_input("                Enter Your Choice [1/2/3/4]  :  "))

      
      if choice == 1 :
           pr = "\n\n          Your Choice is to Create Report Card \n"
           nt = "          Get ready With Student's personal profile ,  Forwarding you to Insert Info Menu "
           print pr, nt
           time.sleep(2)
           os.system("cls")
           print "\n"*8
           time.sleep(0.5)
           print "               Enter Class of student For Which Report card is to be Created \n "
           time.sleep(0.5)
           sec = int(raw_input("               Enter Class  : "))
           os.system("cls")

           if sec > 12:
                  print "\n\n          Wrong Choice Entered (May be greater than 12), Please re-correct "


           else:
                  print "\n\n\n\n"
                  print " "*15,"INSERT INFO \n\n"
                  time.sleep(0.5)
                  print  "  0.      Class Entered  : ",sec
                  name   =  str(raw_input("  1.      Enter Name of the Student :  "))
                  rolln    =             int(raw_input("  2.      Enter Roll Number :  "))
                  adm     =   int(raw_input("  3.      Enter Addmission number :  "))
                  dob     =                  raw_input("  4.      Enter Date of birth :  ")
                  mother =        str(raw_input("  5.      Enter Mother's name  :  "))
                  father  =          str(raw_input("  6.      Enter Father's name  :  "))
                  address=           raw_input("  7.      Enter  Residence address :  ")
                  mob    =       int(raw_input("  8.      Enter Contact number  :  "))
                  time.sleep(1)
                  os.system('cls')
                  print "\n\n\n\n"
                  print "        Now  You  Are  In  Class ",sec

                  if (sec == 11) or (sec == 12):
                      print "\n\n\n\n"
                      print " "*72,"1.      MEDICAL (Science Stream)\n "
                      print " "*72,"2.    NON-MEDICAL (Commerce Stream) \n\n"
                      time.sleep(0.5)
                      print "           Choose Your Subject Stream \n\n"
                      d = int(raw_input("          Enter Your Choice [1/2] : "))
                      time.sleep(0.5)
            
                      if d == 1:
                          os.system('cls')
                          print "\n\n "
                          print "          Create Report Card For :- "," "*58, "1.         UNIT TEST 1"
                          print " "*95, "2.   TERMINAL EXAMINATION 1"
                          print " "*95, "3.         UNIT TEST 2"
                          print " "*95, "4.   TERMINAL EXAMINATION 2\n"
                          time.sleep(1)
                          eng1,eng2,eng3,eng4,phy1,phy2,phy3,phy4,mat1,mat2,mat3,mat4,che1,che2,che3,che4,cs1,cs2,cs3,cs4=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

                          print "          For Which Exam/Test You Want To Enter Entries \n"

                          select = int(raw_input("          Enter Your Choice [1/4] : "))
                          if select == 1:
                              s = "  UNIT TEST 1  "
                          elif select == 2:
                              s = "  TERMINAL EXAMINATION 1  "
                          elif select == 3:
                              s= "  UNIT TEST 2  "
                          elif select == 4:
                              s = "  TERMINAL EXAMINATION 2  "      
                          else:
                              " "      

                          time.sleep(1)
                          os.system('cls')

                          print "\n"
                          print "          Now You Are Creating Report Card's Data Sheet For ",s ,"\n"
                          time.sleep(3)

                          if select == 1:
                              print "          Enter Your Marks Out Of 50\n "
                              eng1 =                             int(raw_input("          Enter Marks of English : ")) 
                              mat1 =                   int(raw_input("          Enter Marks of Maths/Biology : "))
                              cs1   = int(raw_input("          Enter Marks of Computer Sci./Physical Edu. : "))
                              phy1 =                             int(raw_input("          Enter Marks of Physics : "))
                              che1 =                         int(raw_input("          Enter Marks of Chemistry : "))
        
                          elif select == 2:
                              print "          Enter Your Marks Out Of 100\n "
                              eng2 =                            int(raw_input("          Enter Marks of English : "))
                              mat2 =                  int(raw_input("          Enter Marks of Maths/Biology : "))
                              cs2    =int(raw_input("          Enter Marks of Computer Sci./Physical Edu. : "))
                              phy2 =                             int(raw_input("          Enter Marks of Physics : "))
                              che2 =                         int(raw_input("          Enter Marks of Chemistry : "))

                          elif select == 3:
                              print "          Enter Your Marks Out Of 50\n "
                              eng3 =                            int(raw_input("          Enter Marks of English : "))
                              mat3=                   int(raw_input("          Enter Marks of Maths/Biology : "))
                              cs3   =int(raw_input("          Enter Marks of Computer Sci./Physical Edu. : "))
                              phy3 =                            int(raw_input("          Enter Marks of Physics : "))
                              che3 =                        int(raw_input("          Enter Marks of Chemistry : "))

                          elif select == 4:
                              print "          Enter Your Marks Out Of 100\n "
                              eng4 =                            int(raw_input("          Enter Marks of English : "))
                              mat4 =                  int(raw_input("          Enter Marks of Maths/Biology : ")) 
                              cs4   =int(raw_input("          Enter Marks of Computer Sci./Physical Edu. : ")) 
                              phy4 =                            int(raw_input("          Enter Marks of Physics : "))
                              che4 =                         int(raw_input("         Enter Marks of Chemistry : "))

                          else :
                              " "
  
                          rn = rolln
                          ss = "\ "+str(rn)+"Maths"+str(sec)+".txt"
                          print "\n\n "," "*20," Your Data Sheet For Roll No.",rn," Has Been Created.\n"
                          print " "*20," By Filename :- ",str(rn),"Maths",str(sec),".txt"
                          time.sleep(3)

                          f=open( "C:\Python27\Lib\importlib"+ss+"","w")

                          a1 = " "*140+school+" \n\n"
                          f.write(a1)
                          a2 = " "*145+" REPORT CARD\n\n "
                          f.write(a2)
                          a3 = "_"*198+"\n\n"
                          f.write(a3)
                          a4 = " "*5+"Name :- "+name+" \n\n"
                          f.write(a4)
                          a5 = " "*10+"Student's Bio_\n\n "+" "*10+"   Admission No. :-      "+str(adm)+" "*40+"   Roll No. :-      "+str(rolln)
                          f.write(a5)
                          a10 =" "*40+"   Date of Birth :-      "+str(dob)+" "*40+"   Class :-      "+str(sec)+"\n"
                          f.write(a10)
                          a6 = "_"*198+"\n\n"
                          f.write(a6)
                          a7 = " "*10+"Parent's Info_ \n\n"
                          f.write(a7)
                          a8 = " "*10+"      Father's Name :-      "+father+" "*50+"    Mother's Name :-      "+mother+"\n\n"
                          f.write(a8)
                          a9 = " "*10+"      Address :-      "+address+"\n"+" "*10+"      Contact No. :-      "+str(mob)+"\n\n"
                          f.write(a9)

                          zn = "_"*198+"\n\n"
                          f.write(zn)
                          z1=" "*10+"Subject"+" "*55+"Unit test 1"+" "*34+"Terminal Exam 1"+" "*34+"Unit Test 2"+" "*34+"Terminal Exam 2 \n"
                          f.write(z1)
                          zy = "_"*198+"\n\n"
                          f.write(zy)
                          z2=" "*10+"English" +" "*59+str(eng1)+" "*49+str(eng2)+" "*52+str(eng3)+" "*49+str(eng4)+"\n"
                          f.write(z2)
                          z3=" "*10+"Chemistry" +" "*55+str(che1)+" "*49+str(che2)+" "*52+str(che3)+" "*49+str(che4)+"\n"
                          f.write(z3)
                          z4=" "*10+"Physics" +" "*59+str(phy1)+" "*49+str(phy2)+" "*52+str(phy3)+" "*49+str(phy4)+"\n"
                          f.write(z4)
                          z5=" "*10+"Maths/Biology" +" "*49+str(mat1)+" "*49+str(mat2)+" "*52+str(mat3)+" "*49+str(mat4)+"\n"
                          f.write(z5)
                          z6=" "*10+"C.S./P.E." +" "*56+str(cs1)+" "*49+str(cs2)+" "*52+str(cs3)+" "*49+str(cs4)+"\n"
                          f.write(z6)
                          zz = "_"*198+"\n\n"
                          f.write(zz)
                          ut1 = eng1 + che1 + mat1 + cs1 + phy1
                          sa1 = eng2 + che2 + mat2 + cs2 + phy2
                          ut2 = eng3 + che3 + mat3 + cs3 + phy3
                          sa2 = eng4 + che4 + mat4 + cs4 + phy4
                          z7=" "*10+"Total" +" "*58+str(ut1)+"/250"+" "*40+str(sa1)+"/500"+" "*44+str(ut2)+"/250"+" "*42+str(sa2)+"/500"+"\n"
                          f.write(z7)
                          put1 = ut1 * 100 /250 
                          put2 = ut2 * 100/250
                          psa1 = sa1 * 100/500 
                          psa2 = sa2 * 100/500 
                          z8=" "*10+"Total %" +" "*58+str(put1)+"%"+" "*47+str(psa1)+"%"+" "*47+str(put2)+"%"+" "*47+str(psa2)+"%"+"\n"
                          f.write(z8)
                          zx = "_"*198+"\n\n"
                          f.write(zx)
                          f.close()
                          os.system("cls")



                      elif d == 2:
                          os.system('cls')
                          print "\n\n"
                          print "           Create Report Card For :- "," "*57, "1.         UNIT TEST 1"
                          print " "*95, "2.    TERMINAL EXAMINATION 1"
                          print " "*95, "3.         UNIT TEST 2 "
                          print " "*95, "4.    TERMINAL EXAMINATION 2\n"
                          time.sleep(1)
                          eng1,eng2,eng3,eng4,acc1,acc2,acc3,acc4,eco1,eco2,eco3,eco4,bui1,bui2,bui3,bui4,mcp1,mcp2,mcp3,mcp4=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

                          print "          For Which Exam/Test You Want To Enter Entries \n"
                          select = int(raw_input("          Enter Your Choice [1/4] : "))

                          if select == 1:
                              s = "   UNIT TEST 1  "
                          elif select == 2:
                              s = "  TERMINAL EXAMINATION 1  "
                          elif select == 3:
                              s = "   UNIT TEST 2 "
                          elif select == 4:
                              s = "  TERMINAL EXAMINATION 2  "
                          else:
                              " "
     
                          time.sleep(1)
                          os.system('cls')
                          print "\n"
                          print "          Now You are Creating Report Card's Data sheet For",s
                          time.sleep(3)
 

                          print "\n"
                          if select == 1:
                              print "          Enter Your Marks Out Of 50\n "
                              eng1 =                                     int(raw_input("          Enter Marks of English : ")) 
                              mcp1=int(raw_input("          Enter Marks of Maths/Computer Sci./Physical Edu. : ")) 
                              acc1 =                             int(raw_input("          Enter Marks of Accountancy : "))
                              bui1 =                           int(raw_input("          Enter Marks of Business studies : "))
                              eco1 =                                int(raw_input("          Enter Marks of Economics : "))
                          elif select == 2:
                              print "          Enter Your Marks Out Of 100\n "
                              eng2 =                                     int(raw_input("          Enter Marks of English : ")) 
                              mcp2=int(raw_input("          Enter Marks of Maths/Computer Sci./Physical Edu. : ")) 
                              acc2 =                             int(raw_input("          Enter Marks of Accountancy : "))
                              bui2 =                           int(raw_input("          Enter Marks of Business studies : "))
                              eco2 =                                int(raw_input("          Enter Marks of Economics : "))
                          elif select == 3:
                              print "          Enter Your Marks Out Of 50\n "
                              eng3 =                                     int(raw_input("          Enter Marks of English : ")) 
                              mcp3=int(raw_input("          Enter Marks of Maths/Computer Sci./Physical Edu. : "))
                              acc3 =                             int(raw_input("          Enter Marks of Accountancy : "))
                              bui3 =                           int(raw_input("          Enter Marks of Business studies : "))
                              eco3 =                                int(raw_input("          Enter Marks of Economics : "))
                          elif select == 4:
                              print "          Enter Your Marks Out Of 100\n "
                              eng4 =                                     int(raw_input("          Enter Marks of English : ")) 
                              mcp4=int(raw_input("          Enter Marks of Maths/Computer Sci./Physical Edu. : "))
                              acc4 =                              int(raw_input("          Enter Marks of Accountancy : "))
                              bui4 =                            int(raw_input("          Enter Marks of Business studies : "))
                              eco4 =                                  int(raw_input("          Enter Marks of Economics: "))
                          elif select > 4:
                              for select  in range(5,1000):
                                  print "         !!! !!! !!! !!!Select From only 1 , 2 , 3 , 4 !!! !!!! !!! ! "
                                  break
                          else:
                             " "

                          rn = rolln
                          ss = "\ "+str(rn)+"Commerce"+str(sec)+".txt"
                          print "\n\n "," "*20," Your Data Sheet For Roll No.",rn," Has Been Created.\n"
                          print " "*20," By Filename :- ",str(rn),"Commerce",str(sec),".txt"
                          time.sleep(3)
 
                          f=open( "C:\Python27\Lib\importlib"+ss+"","w")
 
                          a1 = " "*140+school+" \n\n"
                          f.write(a1)
                          a2 = " "*145+" REPORT CARD\n\n "
                          f.write(a2)
                          a3 = "_"*198+"\n\n"
                          f.write(a3)
                          a4 = " "*5+"Name :- "+name+" \n\n"
                          f.write(a4)
                          a5 = " "*10+"Student's Bio_\n\n "+" "*10+"   Admission No. :-      "+str(adm)+" "*40+"   Roll No. :-      "+str(rolln)
                          f.write(a5)
                          a10 =" "*40+"   Date of Birth :-      "+str(dob)+" "*40+"   Class :-      "+str(sec)+"\n"
                          f.write(a10)
                          a6 = "_"*198+"\n\n"
                          f.write(a6)
                          a7 = " "*10+"Parent's Info_ \n\n"
                          f.write(a7)
                          a8 = " "*10+"      Father's Name :-      "+father+" "*50+"    Mother's Name :-      "+mother+"\n\n"
                          f.write(a8)
                          a9 = " "*10+"      Address :-      "+address+"\n"+" "*10+"      Contact No. :-      "+str(mob)+"\n\n"
                          f.write(a9)

                          zn = "_"*198+"\n\n"
                          f.write(zn)
                          z1=" "*10+"Subject"+" "*55+"Unit test 1"+" "*34+"Terminal Exam 1"+" "*34+"Unit Test 2"+" "*34+"Terminal Exam 2 \n"
                          f.write(z1)
                          zy = "_"*198+"\n\n"
                          f.write(zy)
                          z2=" "*10+"English" +" "*59+str(eng1)+" "*49+str(eng2)+" "*52+str(eng3)+" "*49+str(eng4)+"\n"
                          f.write(z2)
                          z3=" "*10+"Accounts" +" "*55+str(acc1)+" "*49+str(acc2)+" "*52+str(acc3)+" "*49+str(acc4)+"\n"
                          f.write(z3)
                          z4=" "*10+"Buisness" +" "*58+str(bui1)+" "*49+str(bui2)+" "*52+str(bui3)+" "*49+str(bui4)+"\n"
                          f.write(z4)
                          z5=" "*10+"Maths/C.S./P.E." +" "*46+str(mcp1)+" "*49+str(mcp2)+" "*52+str(mcp3)+" "*49+str(mcp4)+"\n"
                          f.write(z5)
                          z6=" "*10+"Economics" +" "*53+str(eco1)+" "*49+str(eco2)+" "*52+str(eco3)+" "*49+str(eco4)+"\n"
                          f.write(z6)
                          zz = "_"*198+"\n\n"
                          f.write(zz)
                          ut1 = eng1 + acc1 + mcp1 + eco1 + bui1
                          sa1 = eng2 + acc2 + mcp2 + eco2 + bui2
                          ut2 = eng3 + acc3 + mcp3 + eco3 + bui3
                          sa2 = eng4 + acc4 + mcp4 + eco4 + bui4
                          z7=" "*10+"Total" +" "*58+str(ut1)+"/250"+" "*40+str(sa1)+"/500"+" "*44+str(ut2)+"/250"+" "*42+str(sa2)+"/500"+"\n"
                          f.write(z7)
                          put1 = ut1 * 100 /250 
                          put2 = ut2 * 100/250
                          psa1 = sa1 * 100/500 
                          psa2 = sa2 * 100/500 
                          z8=" "*10+"Total %" +" "*58+str(put1)+"%"+" "*47+str(psa1)+"%"+" "*47+str(put2)+"%"+" "*47+str(psa2)+"%"+"\n"
                          f.write(z8)
                          zx = "_"*198+"\n\n"
                          f.write(zx)
                          f.close()
                          os.system("cls")

                      else:
                          print "\n\n          Wrong Choice Entered (May be greater than 2), Please re-correct "
                          os.system('cls')
                  else:
                      print "\n\n"
                      print "          Create Report Card For  :- "," "*47,"1.    Formative Assessment  1"
                      print " "*85,"2.    Formative Assessment  2"
                      print " "*85,"3.    Summative Assessment 1"
                      print " "*85,"4.    Formative Assessment  3"
                      print " "*85,"5.    Formative Assessment  4 "
                      print " "*85,"6.    Summative Assessment 2"
                      print"\n\n"
                      time.sleep(2)

                      Gk1,Gk2,Gk3,Gk4,Gk5,Gk6,Eng1,Eng2,Eng3,Eng4,Eng5,Eng6,Hnd1,Hnd2,Hnd3,Hnd4,Hnd5,Hnd6=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
                      Mat1,Mat2,Mat3,Mat4,Mat5,Mat6,Sci1,Sci2,Sci3,Sci4,Sci5,Sci6=0,0,0,0,0,0,0,0,0,0,0,0,
                      Soc1,Soc2,Soc3,Soc4,Soc5,Soc6,Com1,Com2,Com3,Com4,Com5,Com6=0,0,0,0,0,0,0,0,0,0,0,0,

                      print "          For Which Exam/Test You Want To Enter Entries \n"
                      select = int(raw_input("          Enter Your Choice [1/6] : "))

                      if select == 1:
                          s = " Formative Assessment  1 "
                      elif select == 2:
                          s = " Formative Assessment  2 "
                      elif select == 3:
                          s = " Summative Assessment 1 "
                      elif select == 4:
                          s = " Formative Assessment  3 "
                      elif select == 5:
                          s = " Formative Assessment  4 "
                      elif select == 6:
                          s = " Summative Assessment 2 "
                      else:
                          " Wrong Choice"
      
                      time.sleep(1)
                      os.system('cls')
                      print "\n        Now You are Creating Report Card's Data sheet For",s
                      time.sleep(3)
                      print "\n"

                      if select==1:
                          print "        Enter Your Marks Out Of 20\n "
                          Eng1   =               int(raw_input("          Enter Marks of English : "))
                          Hnd1  =                 int(raw_input("          Enter Marks of Hindi : "))
                          Mat1  =        int(raw_input("          Enter Marks of Mathematics : "))
                          Sci1   =              int(raw_input("           Enter Marks of Science : "))
                          Soc1  =       int(raw_input("          Enter Marks of Social Science : "))
                          Com1 =            int(raw_input("          Enter Marks of Computer : "))
                          Gk1   =int(raw_input("          Enter Marks of General Knowledge : "))

                      if select==2:
                          print "        Enter Your Marks Out Of 20\n "
                          Eng2 =                 int(raw_input("          Enter Marks of English : "))
                          Hnd2 =                  int(raw_input("          Enter Marks of Hindi : "))
                          Mat2 =         int(raw_input("          Enter Marks of Mathematics : "))
                          Sci2  =               int(raw_input("           Enter Marks of Science : "))
                          Soc2 =        int(raw_input("          Enter Marks of Social Science : "))
                          Com2 =            int(raw_input("          Enter Marks of Computer : "))
                          Gk2   =int(raw_input("          Enter Marks of General Knowledge : "))

                      if select==3:
                          print "        Enter Your Marks Out Of 100\n "
                          Eng3  =                  int(raw_input("          Enter Marks of English : "))
                          Hnd3 =                    int(raw_input("          Enter Marks of Hindi : "))
                          Mat3 =           int(raw_input("          Enter Marks of Mathematics : "))
                          Sci3  =                  int(raw_input("          Enter Marks of Science : "))
                          Soc3 =          int(raw_input("          Enter Marks of Social Science : "))
                          Com3 =             int(raw_input("          Enter Marks of Computer : "))
                          Gk3    =int(raw_input("          Enter Marks of General Knowledge : "))

                      if select==4:
                          print "        Enter Your Marks Out Of 20\n "
                          Eng4  =                 int(raw_input("          Enter Marks of English : "))
                          Hnd4 =                   int(raw_input("          Enter Marks of Hindi : "))
                          Mat4 =          int(raw_input("          Enter Marks of Mathematics : "))
                          Sci4  =                 int(raw_input("          Enter Marks of Science : "))
                          Soc4 =         int(raw_input("          Enter Marks of Social Science : "))
                          Com4=             int(raw_input("          Enter Marks of Computer : "))
                          Gk4   =int(raw_input("          Enter Marks of General Knowledge : "))

                      if select==5:
                          print "        Enter Your Marks Out Of 20\n "
                          Eng5  =                 int(raw_input("          Enter Marks of English : "))
                          Hnd5 =                   int(raw_input("          Enter Marks of Hindi : "))
                          Mat5 =          int(raw_input("          Enter Marks of Mathematics : "))
                          Sci5  =                 int(raw_input("          Enter Marks of Science : "))
                          Soc5 =         int(raw_input("          Enter Marks of Social Science : "))
                          Com5=             int(raw_input("          Enter Marks of Computer : "))
                          Gk5  =int(raw_input("           Enter Marks of General Knowledge : "))

                      if select==6:
                          print "        Enter Your Marks Out Of 100\n "
                          Eng6   =                 int(raw_input("          Enter Marks of English : "))
                          Hnd6  =                   int(raw_input("          Enter Marks of Hindi : "))
                          Mat6  =          int(raw_input("          Enter Marks of Mathematics : "))
                          Sci6   =                 int(raw_input("          Enter Marks of Science : "))
                          Soc6  =        int(raw_input("          Enter Marks of Social Science : "))
                          Com6 =            int(raw_input("          Enter Marks of Computer : "))
                          Gk6   =int(raw_input("          Enter Marks of General Knowledge : "))
                      else:
                          "   "

        
                      rn = rolln
                      ss = "\ "+str(rn)+"OneToTen"+str(sec)+".txt"
                      print "\n\n "," "*20," Your Data Sheet For Roll No.",rn," Has Been Created.\n"
                      print " "*20," By Filename :- ",str(rn),"OneToTen",str(sec),".txt"
                      time.sleep(3)
          
                      f=open( "C:\Python27\Lib\importlib"+ss+ "" ,"w" ) 

                      a1 = " "*140+school+" \n\n"
                      f.write(a1)
                      a2 = " "*145+" REPORT CARD\n\n "
                      f.write(a2)
                      a3 = "_"*198+"\n\n"
                      f.write(a3)
                      a4 = " "*5+"Name :- "+name+" \n\n"
                      f.write(a4)
                      a5 = " "*10+"Student's Bio_\n\n "+" "*10+"   Admission No. :-      "+str(adm)+" "*40+"   Roll No. :-      "+str(rolln)
                      f.write(a5)
                      a10 =" "*40+"   Date of Birth :-      "+str(dob)+" "*40+"   Class :-      "+str(sec)+"\n"
                      f.write(a10)
                      a6 = "_"*198+"\n\n"
                      f.write(a6)
                      a7 = " "*10+"Parent's Info_ \n\n"
                      f.write(a7)
                      a8 = " "*10+"      Father's Name :-      "+father+" "*50+"    Mother's Name :-      "+mother+"\n\n"
                      f.write(a8)
                      a9 = " "*10+"      Address :-      "+address+"\n\n"+" "*10+"      Contact No. :-      "+str(mob)+"\n\n"
                      f.write(a9)

                      zn = "_"*198+"\n\n"
                      f.write(zn)
                      z1=" "*10+"Subject"+" "*55+"F.A. 1"+" "*34+"F.A. 2"+" "*34+"S.A. 1"+" "*34+"F.A. 3"+" "*34+"F.A. 4"+" "*34+"S.A. 2\n"
                      f.write(z1)
                      zy = "_"*198+"\n\n"
                      f.write(zy)
                      z2=" "*10+"English""                  "+" "*35+str(Eng1)+" "*42+str(Eng2)+" "*46+str(Eng3)+" "*42+str(Eng4)+" "*42+str(Eng4)+" "*42+str(Eng4)+"\n"
                      f.write(z2)
                      z3=" "*10+"Hindi""                    "+" "*35+str(Hnd1)+" "*42+str(Hnd2)+" "*46+str(Hnd3)+" "*42+str(Hnd4)+" "*42+str(Hnd5)+" "*42+str(Hnd6)+"\n"
                      f.write(z3)
                      z4=" "*10+"Maths""                   "+" "*35+str(Mat1)+" "*42+str(Mat2)+" "*46+str(Mat3)+" "*42+str(Mat4)+" "*42+str(Mat5)+" "*42+str(Mat6)+"\n"
                      f.write(z4)
                      z5=" "*10+"Science""                 "+" "*35+str(Sci1)+" "*42+str(Sci2)+" "*46+str(Sci3)+" "*42+str(Sci4)+" "*42+str(Sci5)+" "*42+str(Sci6)+"\n"
                      f.write(z5)
                      z6=" "*10+"Social Science""        "+" "*35+str(Soc1)+" "*42+str(Soc2)+" "*46+str(Soc3)+" "*42+str(Soc4)+" "*42+str(Soc5)+" "*42+str(Soc6)+"\n"
                      f.write(z6)
                      z7=" "*10+"Computer""             "+" "*35+str(Com1)+" "*42+str(Com2)+" "*46+str(Com3)+" "*42+str(Com4)+" "*42+str(Com5)+" "*42+str(Com6)+"\n"
                      f.write(z7)
                      z8=" "*10+"General Knowledge"""+" "*35+str(Gk1)+" "*42+str(Gk2)+" "*42+str(Gk3)+" "*42+str(Gk4)+" "*42+str(Gk5)+" "*42+str(Gk6)+"\n"
                      f.write(z8)
                      zz = "_"*198+"\n\n"
                      f.write(zz)
                      fa1 = Eng1 + Hnd1 + Mat1 + Gk1 + Sci1 + Com1 + Soc1
                      fa2 = Eng2 + Hnd2 + Mat2 + Gk2 + Sci2 + Com2 + Soc2
                      sa1 = Eng3 + Hnd3 + Mat3 + Gk3 + Sci3 + Com3 + Soc3
                      fa3 = Eng4 + Hnd4 + Mat4 + Gk4 + Sci4 + Com4 + Soc4
                      fa4 = Eng5 + Hnd5 + Mat5 + Gk5 + Sci5 + Com5 + Soc5
                      sa2 = Eng6 + Hnd6 + Mat6 + Gk6 + Sci6 + Com6 + Soc6
                      z9=" "*10+"Total" +" "*58+str(fa1)+"/140"+" "*30+str(fa2)+"/140"+" "*34+str(sa1)+"/700"+" "*37+str(fa3)+"/140"+" "*37+str(fa4)+"/140"+" "*32+str(sa2)+"/700"+"\n"
                      f.write(z9)
                      pfa1 = fa1 * 100 /140 
                      pfa2 = fa2 * 100/140
                      pfa4 = fa4 * 100/140
                      pfa3 = fa3 * 100/140
                      psa1 = sa1 * 100/700 
                      psa2 = sa2 * 100/700 
                      z10=" "*10+"Total %" +" "*56+str(pfa1)+"%"+" "*37+str(pfa2)+"%"+" "*37+str(psa1)+"%"+" "*43+str(pfa3)+"%"+" "*43+str(pfa4)+"%"+" "*43+str(psa2)+"%"+"\n"
                      f.write(z10)
                      zx = "_"*198+"\n\n"
                      f.write(zx)
                      f.close()
                      os.system("cls")

##################################################################################################################################################################################################################






      elif choice == 2:
         pr = "\n\n          Your Choice is to Display A previously saved Report Card \n"
         nt = "          Forwarding you to the Display Menu "
         print pr,nt
         time.sleep(2)
         os.system("cls")
         print "\n"*10
         print "               Enter Class of student For Which Report card is to be Displayed \n "
         time.sleep(1)
         sec = int(raw_input("               Enter Class  : "))

         if sec > 12:
             print "\n\n               Wrong Choice Entered (May be greater than 12), Please re-correct "
             os.system('cls')
      
         elif (sec == 11) or (sec == 12):
             os.system('cls')
             print "\n\n\n\n"
             print " "*72,"1.      MEDICAL (Science Stream)\n "
             print " "*72,"2.    NON-MEDICAL (Commerce Stream) \n\n"
             time.sleep(0.5)
             print "          Choose Your Subject Stream \n"
             d = int(raw_input("          Enter Your Choice [1/2] : "))
             time.sleep(0.5)
             os.system("cls")
             if d == 1:
                 os.system("cls")
                 print "\n"*5
                 print "          Enter Roll No Of The Student Whose Report Card Is To Be Displayed "
                 rn = int(raw_input("          Enter Roll No : "))
                 ss ="\ "+str(rn)+"Maths"+str(sec)+".txt"
                 print "\n"
                 time.sleep(1)
                 print "          Your Report Card For Roll No.",rn," Is Ready To Be Displayed"
                 time.sleep(5)
                 os.system("cls")


                 
                 Tk=Tk()
                 sch=Text(Tk,height = 1600,width = 900, fg="pink",bg="black",font=('Albertus Medium',13))
                 sch.pack()
                 f=open( "C:\Python27\Lib\importlib"+ss+"","r")
                 sch.insert(END,f.read())
                 f.close()
                 mainloop()

             elif d == 2:
                 os.system("cls")
                 print "\n"*5
                 print "          Enter Roll No Of The Student Whose Report Card Is To Be Displayed "
                 rn = int(raw_input("          Enter Roll No : "))
                 ss ="\ "+str(rn)+"Commerce"+str(sec)+".txt"
                 print "\n"
                 time.sleep(1)
                 print "          Your Report Card For Roll No.",rn," Is Ready To Be Displayed"
                 time.sleep(5)
                 os.system("cls")


                 
                 Tk=Tk()
                 sch=Text(Tk,height = 1600,width = 900, fg="white",bg="black",font=('Albertus Medium',13))
                 sch.pack()
                 f=open( "C:\Python27\Lib\importlib"+ss+"","r")
                 sch.insert(END,f.read())
                 f.close()
                 mainloop()
             else:
                 print "\n\n               Wrong Choice Entered (May be greater than 12), Please re-correct "
                 os.system('cls')

         else:
             os.system("cls")
             print "\n"*5
             print "          Enter Roll No Of The Student Whose Report Card Is To Be Displayed "
             rn = int(raw_input("          Enter Roll No : "))
             ss ="\ "+str(rn)+"OneToTen"+str(sec)+".txt"
             print "\n"
             time.sleep(1)
             print "          Your Report Card For Roll No.",rn," Is Ready To Be Displayed"
             time.sleep(5)
             os.system("cls")


             
             Tk=Tk()
             sch=Text(Tk,height = 1600,width = 900, fg="brown",bg="white",font=('Albertus Medium',13))
             sch.pack()
             f=open( "C:\Python27\Lib\importlib"+ss+"","r")
             sch.insert(END,f.read())
             f.close()
             mainloop()


             os.system("cls")
         raw_input("          Press Enter Button To Continue With Program ")
         os.system("cls")
            
      elif choice == 3:
             pr = "\n\n          Your Choice is to Delete A Report Card \n"
             nt = "          Forwarding you to the Delete Menu "
             print pr,nt
             time.sleep(2)
             os.system("cls")
             print "\n"*10
             print "               Enter Class of student For Which Report card has to be Deleted \n "
             time.sleep(1)
             sec = int(raw_input("               Enter Class  : "))
             if sec > 12:
                   print "\n\n               Wrong Choice Entered (May be greater than 12), Please re-correct "
                   os.system('cls')
             elif (sec == 11) or (sec == 12):
                   os.system('cls')
                   print "\n\n\n\n"
                   print " "*72,"1.      MEDICAL (Science Stream)\n "
                   print " "*72,"2.    NON-MEDICAL (Commerce Stream) \n\n"
                   time.sleep(0.5)
                   print "          Choose Your Subject Stream \n"
                   d = int(raw_input("          Enter Your Choice [1/2] : "))
                   time.sleep(0.5)
                   os.system("cls")
                   if d == 1:
                         os.system("cls")
                         print "\n"*5
                         print "          Enter Roll No Of The Student Whose Report Card Has To Be Deleted "
                         rn = int(raw_input("          Enter Roll No : "))
                         ss ="\ "+str(rn)+"Maths"+str(sec)+".txt"
                         print "\n"
                         time.sleep(1)
                         dss="C:\Python27\Lib\importlib"+ss+""
                         os.remove(dss)
                         print "          Your Report Card For Roll No.",rn," Is Deleted"
                         time.sleep(5)
                         os.system("cls")

                   if d == 2:
                         os.system("cls")
                         print "\n"*5
                         print "          Enter Roll No Of The Student Whose Report Card Has To Be Deleted "
                         rn = int(raw_input("          Enter Roll No : "))
                         ss ="\ "+str(rn)+"Commerce"+str(sec)+".txt"
                         print "\n"
                         time.sleep(1)
                         dss="C:\Python27\Lib\importlib"+ss+""
                         os.remove(dss)
                         print "          Your Report Card For Roll No.",rn," Is Deleted"
                         time.sleep(5)
                         os.system("cls")
                   else:
                         print "\n\n               Wrong Choice Entered (May be greater than 12), Please re-correct "
                         os.system('cls')

             else:
                  os.system("cls")
                  print "\n"*5
                  print "          Enter Roll No Of The Student Whose Report Card Has To Be Deleted "
                  rn = int(raw_input("          Enter Roll No : "))
                  ss ="\ "+str(rn)+"OneToTen"+str(sec)+".txt"
                  print "\n"
                  time.sleep(1)
                  dss="C:\Python27\Lib\importlib"+ss+""
                  os.remove(dss)
                  print "          Your Report Card For Roll No.",rn," Is Deleted"
                  time.sleep(5)
                  os.system("cls")
             raw_input("          Press Enter Button To Continue With Program ")
             os.system("cls")

      elif choice == 4:
         print "\n\n          Exit Option Selected , Terminating Program.... "
         time.sleep(3)
         exit()
                 
  
      else:
         print "\n\n          Wrong Choice Entered (May be greater than 3), Please re-correct \n"
         time.sleep(2)
         raw_input("           Press Enter To Correct it ")
         os.system('cls')
            
####################################################################################################################################################################################################################
