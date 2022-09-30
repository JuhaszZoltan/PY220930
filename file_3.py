pw = 'PassWord123'

psz = 0
while psz < 3 and input('írd be a jelszavad: ') != pw:
    print('téves jelszó!')
    psz += 1

if psz < 3:
    print('sikeres bejelentkezés')
else:
    print('valami nem stimmel!') 
    print('beszélj a rendszergazdával')