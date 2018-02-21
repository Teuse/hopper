import vim
import os
import sys

#--------------------------------------------------------------------------
#--- Helper functions
#--------------------------------------------------------------------------
def fileExt(filePath):
    return os.path.splitext(filePath)[1][1:]

#--------------------------------------------------------------------------
def hasExt(filePath, extList):
    ext = fileExt(filePath)
    return any(ext in s for s in extList)

#--------------------------------------------------------------------------
def changeExtension(filePath, newExt):
    pathWithoutExt = os.path.splitext(filePath)[0]
    return pathWithoutExt + "." + newExt


#--------------------------------------------------------------------------
#--- Algorithmus
#--------------------------------------------------------------------------
def findFileWithExt(filePath, extList):
    for ext in extList:
        newPath = changeExtension(filePath, ext)
        if os.path.isfile(newPath):
            return newPath
    return ""

#--------------------------------------------------------------------------
def findCounterpart(filePath, folderNameList, extList):

    # Search for the counterpart in the current dir...
    newPath = findFileWithExt(filePath, extList)
    if newPath:
        return newPath

    # Search file in other folder structure
    pathIter = filePath
    breakIdx = 8
    while pathIter and pathIter != "/" and pathIter != os.path.expanduser("~") and breakIdx:

        # remove last path component to upward-iterate the folder structure
        pathIter = os.path.dirname(pathIter)
        breakIdx   = breakIdx - 1

        for newFolder in folderNameList:
            curFolder = os.path.basename(pathIter)
            newPath = filePath.replace(curFolder, newFolder)
            newPath = findFileWithExt(newPath, extList)
            if newPath:
                return newPath



#--------------------------------------------------------------------------
#--- Execute script
#--------------------------------------------------------------------------

filePath = vim.eval("expand('%:p')")
if not filePath: sys.exit()

implExtList      = vim.eval("g:hopper_impl_file_ext")
implFolderList   = vim.eval("g:hopper_impl_folder_names")
headerExtList    = vim.eval("g:hopper_header_file_ext")
headerFolderList = vim.eval("g:hopper_header_folder_names")


newPath = ''

if hasExt(filePath, headerExtList):
    newPath = findCounterpart(filePath, implFolderList, implExtList)
elif hasExt(filePath, implExtList):
    newPath = findCounterpart(filePath, headerFolderList, headerExtList)
else:
    print("Hopper: Cant identify file. Maybe it has a unknown file extension")
    sys.exit()


if newPath:
    print("Hopper: Open file: %s" % newPath)
    vim.command(":w ")
    vim.command("edit " + newPath)
else:
    print("Hopper: Cant find counterpart")

