import os

def date_control(val,dateformat="%d-%m-%Y"):
    if type(val)==str:
        try:
            return datetime.strptime(val, dateformat)
        except:
            return val

def read_csv(file,encoding= "ISO-8859-1",delimiter=";",dateformat="%d-%m-%Y"):
    cn=[]

    if not os.path.isfile(file):
        print("File does not exist")
        return cn

    if not str(file).endswith(".csv"):
        print("File extension is not CSV")
        return cn

    with open(file,"r",encoding= encoding) as f:
        lines=f.readlines()
        cols=list(lines[0].strip().split(delimiter))
        sz_cols=len(cols)
        for i in range(1,len(lines)):
            d=list(lines[i].split(delimiter))
            stg = {
                cols[y]: date_control(d[y], dateformat=dateformat)
                for y in range(sz_cols)
            }

            cn.append(stg)
    return cn
def remove_duplicates(cn):
    stg=[]
    for i in cn:
        if stg.count(i)==0:
            stg.append(i)
    return stg
def merge_list(df1,df2,remove_duplicates=True):
    cn=[]
    cols_list=remove_duplicates(list(df1[0].keys()) + list(df2[0].keys()) )
    sz_df1=len(df1)
    df1_cols=list(df1[0].keys())
    df2_cols=list(df2[0].keys())
    for i in range(sz_df1):
        stg = {y: df1[i][y] if y in df1_cols else None for y in cols_list}
        cn.append(stg)
    for i in range(sz_df2):
        stg = {y: df2[i][y] if y in df2_cols else None for y in cols_list}
        cn.append(stg)   

    if remove_duplicates:
        cn=remove_duplicates(cn)
    return cn
    
def change_column_name(ls,old_column,new_column):
    cn=[]
    size=len(ls)
    cols=list(ls[0].keys())
    for i in range(size):
        d=ls[i]
        stg={}
        for y in cols:
            if y==old_column:
                stg[new_column]=d[y]
            else:
                stg[y]=d[y]
                
        cn.append(stg)
    return cn
        
def change_float(val,decimal="."):
    if type(val) == str and val.count(",") > 0:
        val=str(val).replace(",",".")
        try:
            return float(val)
        except:
            return val
    return val

def columns_sum(ls,cols_list,cols_multip,new_column,decimal="."):
    cn=[]
    size=len(ls)
    cols=list(ls[0].keys())
    size_cl=len(cols_list)
    for i in range(size):
        d=ls[i]
        stg = {y: d[y] for y in cols}
        u = sum(
            (
                float(change_float(d[cols_list[k]]))
                * float(change_float(cols_multip[k]))
            )
            for k in range(size_cl)
        )

        stg[new_column]=u
        cn.append(stg)
    return cn
