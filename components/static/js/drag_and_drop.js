function dragDrop() {
    const piecesElements = document.querySelectorAll(".piece");
    const blacksElements = document.querySelectorAll(".black");

    let element;
    let id_start_cell

    piecesElements.forEach(elem => {
        elem.draggable = true;

        elem.addEventListener("dragstart", (e => {
            e.dataTransfer.setData("text/html", "dragstart");
            element = e;
            id_start_cell = e.target.parentNode.id;
        }));
    })

    blacksElements.forEach(elem => {
        elem.addEventListener("dragover", (e => {
            e.preventDefault();
        }));
        elem.addEventListener("drop", (e => {
            if (!e.target.innerHTML.trim() && e.target.classList.contains('black')) {
                e.target.appendChild(element.target);
                element = null;
                document.getElementById(id_start_cell).innerHTML = "";

                let [from_x, from_y] = id_start_cell.split("-");
                let [to_x, to_y] = e.target.id.split("-");

                socket.emit('step', {
                    "from_x": parseInt(from_x),
                    "from_y": parseInt(from_y),
                    "to_x": parseInt(to_x),
                    "to_y": parseInt(to_y)
                });

            }
        }));
    })
};

