print ('This script is based on the guide made by district 969')
print ('http://steamcommunity.com/sharedfiles/filedetails/?id=555942154')

D = input('Input your weapons damage: ')
M = input ('Input your weapons magazine size: ')
ROF = input ('Input your weapons Rate of Fire: ')
R = input ('Input your weapons reload speed (excluding any skills and badass rank): ')
A = input ("Input your weapons accuracy(Let's assume you have perfect aim): ")
ES = input ('Input your weapons elemental splash (They go towards the "splish splash" challange); ')
EDM = input ('Input your weapons elemental damage modifier (eg. shock towards shields set to 1 if none): ')
EEC = input ('Input your weapons elemental effect chance (eg. 0.5=50%): ')
PS = input ("Input your weapons projectile speed (fire a rocket from outside Marcus' gunshop to moxxi's bar and time it, if you are lazy or using bullets input 0.1): ")
DOTM = input ('Input your weapons damage over time damage (how much damage is initially dealt to an enemy hit with a DoT): ')
DOTTIME = input ('Input how long you DoT lasts: ')

d = int(D)
m = int(M)
rof = int(float(ROF))
r = int(R)
a = int(float(A))
es = int(ES)
edm = int(EDM)
eec = int(float(EEC))
ps = int(float(PS))
dotm = int(DOTM)
dottime = int(DOTTIME)

##print (d)
##print (m)
##print (rof)
##print (r)
##print (a)
##print (es)
##print (edm)
##print (eec)
##print (ps)
##print (dotm)
##print (dottime)

Answer1 = eec * dotm * dottime
if Answer1 > 0:
    Answer2 = edm / Answer1
else:
    Answer2 = 1
Answer3 = d * Answer2

answer1 = m * r * ps
if answer1 > 0:
    answer2 = rof / answer1
else:
    answer2 = rof
answer3 = es * answer2
answer4 = answer3 / a

Answer = Answer3 + answer4

#Answer = (d*(edm/(eec*dotm*dottime))+es*(rof/(m*r*ps))/a)

print (Answer)
