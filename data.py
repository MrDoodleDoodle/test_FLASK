import time
class Data():
    def search2(self, d, keyword, i, i_max):
        i+=1
        keys = d.keys()
        open = False
        for key in keys:
            if key != "color" and key != "open":
                d[key]["open"] = False
                d[key]["color"] = False
                #print(key)
                if keyword.lower() in key.lower():
                    d[key]["color"] = True
                    open = True
                if i<i_max:
                    if self.search2(d[key], keyword, i, i_max):
                        d[key]["open"] = True
                        open = True
                else:
                    d[key] = {"open": False, "color": False}
        return open

    def write_file(self,d,f,keyword):
        keys = d.keys()
        for key in keys:
            if key != "color" and key != "open":
                if d[key]["open"]:
                    if len(d[key].keys()) !=2:
                        s = key.replace(keyword, "<mark>" + keyword + "</mark>")
                        f.write(f"""<details open class="c1"> \n  <summary>{s}</summary> \n""")
                        self.write(d[key], f, keyword)
                        f.write(f"</details>\n")
                    else:
                        s = key.replace(keyword, "<mark>" + keyword + "</mark>")
                        f.write(f"""<li class="c2"> \n{s}\n </li> \n""") 
                else:
                    if len(d[key].keys()) !=2:
                        s = key.replace(keyword, "<mark>" + keyword + "</mark>")
                        f.write(f"""<details class="c1"> \n  <summary>{s}</summary> \n""")
                        self.write(d[key], f, keyword)
                        f.write(f"</details>\n")
                    else:
                        s = key.replace(keyword, "<mark>" + keyword + "</mark>")
                        f.write(f"""<li class="c2"> \n{s}\n </li> \n""") 

    def myreplace(self, text, keyword):
        s = text.lower()
        output = ""
        while s.find(keyword.lower()) != -1:
            output += text[:s.find(keyword.lower())] + "<mark>"+text[s.find(keyword.lower()):s.find(keyword.lower())+len(keyword)]+"</mark>"
            i = s.find(keyword.lower())+len(keyword)
            s = s[i:]
            text = text[i:]
        return output+text

    def write(self, d, f, keyword):
        keys = d.keys()
        for key in keys:
            if key != "color" and key != "open":
                if d[key]["open"]:
                    #s = key.replace(keyword, "<mark>" + keyword + "</mark>")
                    s = self.myreplace(key, keyword)
                    f.write(f"""<details open class="c1"> \n  <summary>{s}</summary> \n""")
                    self.write(d[key], f, keyword)
                    f.write(f"</details>\n")

                else:
                    #s = key.replace(keyword, "<mark>" + keyword + "</mark>")
                    s = self.myreplace(key, keyword)
                    f.write(f"""<details class="c1"> \n  <summary>{s}</summary> \n""")
                    self.write(d[key], f, keyword)
                    f.write(f"</details>\n")

    def makedic(self, d, lines):#
        prev = 0
        for i, line in enumerate(lines):
            if line.split(" ")[0] == "â”œâ”€â”€" or line.split(" ")[0] == "â””â”€â”€":
                if prev:
                    d[prev]= self.makedic({}, prev_lines)
                split = line.split(" ")
                name = ""
                for s in split[1:]:
                    name += s +" "
                prev = name.split("\n")[0]
                prev_lines = []
            elif line[:3] == "â”‚": 
                #print(line.split("â”‚   "))
                if line != "" and line[0]!= " ":
                    #print(line)
                    line = line.split("â”‚   ", 1)[1]#.lstrip()
                    prev_lines.append(line)

            elif line[:4] == "    ":
                line = line[4:]
                prev_lines.append(line)

        if prev:
            d[prev]= self.makedic({}, prev_lines)
        return d

    def combine(self, filename, keyword, depth):
        f = open(filename, "r")
        Lines = f.readlines()
        data = self.makedic({}, Lines)
        self.search2(data, keyword, 0, depth)
        f = open("templates//search_page.html", "w")
        f.write("""{% extends 'base.html' %}\n""")
        f.write("""{% block body %}\n""")
        f.write("""<link rel="stylesheet" href="{{url_for('static', filename='css/style.css') }}">""")
        Data().write(data, f, keyword)
        f.write("""{% endblock %}""")
        f.close

    def combine2(self, d, keyword, depth):
        d1 = dict(d)
        self.search2(d1, keyword, 0, depth)
        f = open("templates//search_page.html", "w")
        f.write("""{% extends 'base.html' %}\n""")
        f.write("""{% block body %}\n""")
        #f.write(f"""<form method="POST"><input type="submit" name="depth" value={depth}></form>""")
        f.write("""<link rel="stylesheet" href="{{url_for('static', filename='css/style.css') }}">""")
        Data().write(d1, f, keyword)
        f.write("""{% endblock %}""")
        f.close


# d = Data()
# start_time = time.time()
# #d.combine('all_file_structure.txt', 'a')
# d.makedic({}, open('all_file_structure.txt', "r").readlines())
# print(time.time()-start_time)
# f = open('all_file_structure.txt', "r")
# Lines = f.readlines()
# dic = d.makedic({}, Lines)

# def dict_depth(dic, level = 1):
     
#     if not isinstance(dic, dict) or not dic:
#         return level
#     return max(dict_depth(dic[key], level + 1)
#                                for key in dic)
  
# print(dict_depth(dic))

# d = Data()
# d.combine("file_structure.txt", "datatatatatata")
# f = open("file_structure.txt", "r")
# Lines = f.readlines()
# #print(f.read()) 
# data = Data().makedic({}, Lines)




# #print(data)
# Data().search2(data, "data")
# #print(data)

# f = open("tes.html", "w")
# f.write("""<link rel="stylesheet" href="style.css">""")
# Data().write(data, f, "data")
# f.close