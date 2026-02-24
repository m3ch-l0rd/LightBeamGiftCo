

let postBoard = document.getElementById("postBoard");
let postBasket = JSON.parse(localStorage.getItem("data")) || [];


let generatePostBoard = () => {

    return (postBoard.innerHTML = posts.map((x) => {

        let {img, date, title, para} = x;
        let search = postBasket.find((x) => x.date === date) || [];

        return `
        <div class="post">
            <img id="postImg" src="${img}"></img>
            <div>
                <h3>${date}</h3>
                <h3>${title}</h3>
                <p>${para}</p>
            </div>
        </div>`;
        }).join(""));
     };


generatePostBoard();
