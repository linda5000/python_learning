import cx_Oracle
tns=cx_Oracle.makedsn('10.10.100.234',1521,'wlzy')
db=cx_Oracle.connect('sm','sm',tns)
cr=db.cursor()

pr = {'zc_no':'000013008605'}
sql='select * from zc_sm where ASSETSCARDCODE =:zc_no'
cr.execute(sql,pr)
rs=cr.fetchall()
print(rs)
for i in rs:
    print(i)
cr.close()
db.close()
