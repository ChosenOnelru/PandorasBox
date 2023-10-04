import re

def is_lock_ness_monster(string):
    rez1 = re.findall("3.50", string)
    rez2 = re.findall("three fifty", string)
    rez3 = re.findall("tree fiddy", string)
    #print(rez1, rez2, rez3)
    return bool(rez1) + bool(rez2) + bool(rez3)


print(is_lock_ness_monster("Your girlscout cookies are ready to ship. Your total comes to tree fiddy"))
print(is_lock_ness_monster("Howdy Pardner. Name's Pete Lexington. I reckon you're the kinda stiff who carries about tree fiddy?"))
print(is_lock_ness_monster("I'm from Scottland. I moved here to be with my family sir. Please, $3.50 would go a long way to help me find them"))
print(is_lock_ness_monster("Yo, I heard you were on the lookout for Nessie. Let me know if you need assistance."))
print(is_lock_ness_monster("Did I ever tell you about my run with that paleolithic beast? He tried all sorts of ways to get at my three dolla and fitty cent? I told him 'this is MY 4 dolla!'. He just wouldn't listen."))


