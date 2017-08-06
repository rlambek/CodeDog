######## Native CodeDog library

requirements = [
    [require, GUI_ToolKit_implementation]
]


struct stringScanner{
    me string: S
    me int: pos
    void: init(me string: str) <- {S<-str  reset()}
    void: reset() <- {pos<-0}

    me int: skipWS() <- {       /- Skip past 0 or more whitespace characters.  Return the new pos
        me char: ch
        me uint32: txtSize <- S.size()
        withEach p in RANGE(pos .. txtSize):{
            ch <- S[p]
            if(! isspace(ch) or p==txtSize){pos<-p break()}
        }
        return(pos)
    }

    me int: skipPast(me string: findStr) <- {       /- Skip past <txt>.  Return pos or -1 if End-of-string reached
        me char: ch
        me uint32: txtSize <- S.size()
        me uint32: fs <- findStr.size()
        withEach p in RANGE(pos .. txtSize):{
            withEach i in RANGE(0 .. fs):{
                /-print(">> fs/p/i:", fs, " ", p, " ", i, ", findStr[i]:", findStr[i], " S[p+i]:", S[p+i], "\n")
                if( findStr[i] != S[p+i]) {
                    break()
                } else {if(i==(fs-1)) {pos <- p+fs return(pos)}}
            }
        }
        return(-1)
    }

    me int: skipTo(me string: findStr) <- {       /- Skip up to <txt>.  Return pos or -1 if End-of-string reached
        me int: foundPos <- skipPast(findStr)
        if(foundPos > 0) {return(foundPos-findStr.size())}
        else {return(-1)}
    }

    me int: chkStr(me string: s) <- {
        me int: L <- s.size()
        if(pos+L > S.size()){return(-1)}
        withEach i in RANGE(0 .. L):{
            if( s[i] != S[pos+i]) {
                return(-1)
            }
        }
        pos <- pos+L
        return(pos)
    }
}