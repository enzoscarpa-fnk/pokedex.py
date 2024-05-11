
# AUDIO CRIES FUNCTION ---------------

c.execute('SELECT * FROM Kanto WHERE PK_Index = 025')
pikachu = c.fetchone()
print(pikachu)

cry_qry = ('SELECT Pokemon_CryPath FROM Kanto WHERE PK_Index = 025')
c.execute(cry_qry)
crypath=c.fetchone()[0]
print(crypath)

pygame.mixer.init()
pygame.mixer.music.load(open(crypath))
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(1)
print("done")


# SEARCH FUNCTION ------------------

c.execute("SELECT * FROM Kanto WHERE Pokemon_Name = '{}'".format(sv_search.get()))
result = c.fetchone()
print(result[2])