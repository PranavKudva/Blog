function handleUpdateTitle(){
    toggleUpdateButtonVisibility();
    toggleUpdateInputVisibility();
}

function toggleUpdateButtonVisibility(){
    if(document.getElementById('updateTitle').style.visibility == "hidden")
        document.getElementById('updateTitle').style.visibility = "visible"

    else
        document.getElementById('updateTitle').style.visibility = "hidden"
}

function toggleUpdateInputVisibility(){
    if(document.getElementById('newTitle').type == "hidden")
       newTitle.setAttribute('type', 'text')
    else
       newTitle.setAttribute('type', 'hidden')
}