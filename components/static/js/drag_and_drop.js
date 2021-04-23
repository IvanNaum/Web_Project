function dragDrop() {
    const piecesElements = document.querySelectorAll(".piece");
    const blacksElements = document.querySelectorAll(".black");

    let element;

    piecesElements.forEach(elem => {
        elem.draggable = true;

        elem.addEventListener("dragstart", (e => {
            e.dataTransfer.setData("text/html", "dragstart");
            element = e.target;
        }));
    })

    blacksElements.forEach(elem => {
        elem.addEventListener("dragover", (e => {
            e.preventDefault();
        }));
        elem.addEventListener("drop", (e => {
            if (!e.target.innerHTML.trim() && e.target.classList.contains('black')) {
                e.target.appendChild(element);
            }
        }));
    })
};

