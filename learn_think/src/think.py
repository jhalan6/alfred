# -*- coding: utf-8 -*-

import alfred,sys,json,commands


def main():
    #read
    knowledge_dir = '~/Knowledges'
    query = sys.argv[1:]
    result = "grep -r key %s" % knowledge_dir
    for argu in query:
        if argu:
            result += "| grep "+ argu
    (status, output) = commands.getstatusoutput(result)
    result = []

    i = 1
    for line in output.split('\n') :
        if line:
            file_name = line.split(':')[0]
            key_list = line.split(':')[1].decode('utf8')
            preview = commands.getoutput("cat %s | grep title" % file_name).decode('utf8')
            result.append(alfred.Item({"uid": alfred.uid(i), 'arg': file_name},
                                    key_list, preview, None))
            i=i+1

    if not result:
        result.append(alfred.Item({"uid": alfred.uid(i)},
                                    "nothing find", "", None))

    alfred.write(alfred.xml(result))


if __name__ == "__main__":
    main()
