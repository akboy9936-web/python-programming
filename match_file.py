file=input("enter the file extension:")
match file:
    case 'py':print("python file")
    case 'c':print("c file")
    case 'c++':print("c++ file")
    case 'html':print("HTML file") 
    case 'jpg':print("image file")
    case '_':print("unknown file")