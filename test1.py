if __name__ == "__main__":
    
    ra = {639}
    for s in range(100, 999):
        c = int(s%10)
        b = int(s%100/10)
        a = int(s%1000/100)
        
        n11 = (c*c)%10
        
        if(n11 == c):
            n11o = int(c*c/10)
            n12 = (c*b + n11o)%10
            n12o = int((c*b + n11o)/10)
            n13 = (c*a + n12o)%10
            
            n21 = (b*c)%10
            
            if(((n12 + n21)%10) == b):
                
                n21o = int((b*c)/10)
                n22 = (b*b + n21o)%10
                
                n31 = (c*a)%10
                
                c1 = n11
                b1 = (n12 + n21)%10
                b1o = int((n12 + n21)/10)
                a1 = (n13 + n22 + n31 + b1o)%10
                
                if(a1 == a):
                    print(s)
