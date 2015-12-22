#/////////////////////////////////////////////////  R o u t i n e s   t o   G e n e r a t e  " m a i n ( ) "

import progSpec
import codeDogParser

mainFuncCode=r"// No Main given"
def apply(objects, tags, parserSpecTag):
    initCode=tags['initCode']
    deinitCode=tags['deinitCode']
    tags['Include'] += ",<signal.h>"

    initFuncCode=r"""
    me void: initialize () = {
        %s
    }

    me void: deinitialize () = {
       %s
    }
    """ % (initCode, deinitCode)


    mainFuncCode="""
    me int32: main(me int32: argc, me int32: argv ) = <%{
    initialize();
    signal(SIGSEGV, reportFault);
    drawLine dl;
    dl.DrawLine();
    deinitialize();
    return 0;
 /*   string inputFilename="testInfon.pr";
    fstream fileIn("testInfon.pr");
    if (!fileIn.is_open()){cout<<"Could not open "<<inputFilename<<".\n"; exit(1);}
    infonParser parser;
    parser.stream=&fileIn;
    streamSpan cursor;
    shared_ptr<infon> topInfon=make_shared<infon>();
    parser.BatchParse(&cursor, topInfon.get());
*/

    return 0;
    } %>

"""

    progSpec.addObject(objects[0], objects[1], 'MAIN', 'struct', 'SEQ')
    codeDogParser.AddToObjectFromText(objects[0], objects[1], progSpec.wrapFieldListInObjectDef('MAIN', initFuncCode + mainFuncCode ))
