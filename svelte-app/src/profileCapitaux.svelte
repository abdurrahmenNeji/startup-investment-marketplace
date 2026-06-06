<script>
  import { Link } from 'svelte-routing';
    let client_id = 1; // ID du client
let message = ''; // Message pour afficher le statut de l'opération
let messageColor = ''; // Couleur du message (vert ou rouge)
const token = 'f8d3a3e8643875a8f372a9e51716f12b28ff9752'; // Remplacez par le jeton généré

// Fonction pour gérer l'achat
const acheterArticle = async (articleId) => {
  try {
    console.log("Tentative d'achat de l'article:", articleId);  // Log pour tester
    const response = await fetch('http://127.0.0.1:8000/achats/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${token}`,
      },
      body: JSON.stringify({
        client: client_id,  // Assurez-vous d'envoyer l'ID du client
        article: articleId,  // Assurez-vous d'envoyer l'ID de l'article
        quantite: 1,  // Ajoutez la quantité, si nécessaire
      }),
    });

    if (response.ok) {
      const data = await response.json();
      console.log("Achat ajouté avec succès", data);
      message = "Achat ajouté avec succès!";
      messageColor = 'green';  // Pour changer la couleur
    } else {
      const errorText = await response.text();
      console.log("Erreur lors de l'ajout de l'achat, code : ", response.status);
      console.log("Détail de l'erreur :", errorText);
      message = `Erreur lors de l'ajout de l'achat. Code: ${response.status}`;
      messageColor = 'red';
    }
  } catch (error) {
    console.error("Une erreur est survenue dans le try-catch : ", error);
    message = "Une erreur est survenue.";
    messageColor = 'red';
  }
};
// Définition du tableau de projets
    let projets = [
      { id: 1, nom: "Souris Ergonomique", prix: 10, image: "images/souris.png" },
      { id: 2, nom: "Imprimante Laser Multifonction", prix: 20, image: "images/imprimant.png" },
      { id: 3, nom: "Ordinateur de Bureau Hautes Performances", prix: 30, image: "images/pc.png" },
      { id: 4, nom: "Accessoires de Gaming", prix: 40, image: "images/gaming.png" }
    ];
  </script>
   <style>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

.container {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
    color: #007bff; /* Couleur bleue pour les titres */
}
h1 {
   
    color:#333; /* Couleur bleue pour les titres */
}

.project-list {
    list-style: none;
    padding: 0;
}

.project-item {
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 10px;
    margin-bottom: 10px;
}

.project-item h3 {
    margin-top: 0;
}

.project-item p {
    margin: 5px 0;
}

.btn {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 8px 15px;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
}

.btn:hover {
    background-color: #0056b3;
}

/* Header styles */
header {
    background-color: #f90; /* Changement de la couleur de fond en orange */
    padding: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header h1 {
    font-size: 24px;
    color: white;
    margin-bottom: 10px;
}

.nav form {
    margin-right: 10px;
}

.nav input[type="text"] {
    padding: 8px;
    border: none;
    border-radius: 5px;
    margin-right: 5px;
}

.nav input[type="submit"] {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 5px;
    cursor: pointer;
}

.nav a {
    color: white;
    text-decoration: none;
    margin-right: 10px;
}

.nav img {
    width: 30px;
    height: 30px;
    border-radius: 50%;
    margin-right: 5px;
}

main.table {
    width: 82vw;
    height: 90vh;
    background-color: rgba(255, 255, 255, 0.158);
    backdrop-filter: blur(7px);
    box-shadow: 0 .4rem .8rem rgba(0, 0, 0, 0.333);
    border-radius: .8rem;
    margin-left: 100px;
    overflow: hidden;
}

.table__header {
    width: 100%;
    height: 10%;
    background-color: rgba(17, 16, 16, 0.338);
    padding: .5rem 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.table__body {
    width: 95%;
    max-height: calc(89% - 1.6rem);
    background-color: #f5f5dc; /* Changer en beige clair */
    margin: .5rem auto;
    border-radius: .6rem;
    overflow: auto;
    overflow: overlay;
}

.table__body::-webkit-scrollbar{
    width: 0.5rem;
    height: 0.5rem;
}

.table__body::-webkit-scrollbar-thumb{
    border-radius: .5rem;
    background-color: #0004;
    visibility: hidden;
}

.table__body:hover::-webkit-scrollbar-thumb{ 
    visibility: visible;
}

table {
    width: 100%;
    border-collapse: collapse;
}

td, th {
    padding: 8px; /* Ajustement du padding pour une apparence plus spacieuse */
    text-align: left;
}

thead {
    background-color: #f5deb3; /* Beige clair pour le thead */
    color: #333; /* Texte plus foncé pour contraste */
}

thead th {
    cursor: pointer;
    text-transform: capitalize;
    font-size: 15px;
    padding: 12px; /* Ajustement du padding pour une apparence plus spacieuse */
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

tr:hover {
    background-color: #ddd;
}

.btn {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 8px 15px;
    border-radius: 5px;
    cursor: pointer;
    text-decoration: none;
    transition: background-color 0.3s;
}

.btn:hover {
    background-color: #0056b3;
}
.add-project-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 50%;
    font-size: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    text-decoration: none;
}

.add-project-btn:hover {
    background-color: #0056b3;
}


    </style>

  
<header>
    
     
  <h1>Bienvenue sur votre compte !</h1>
  <div class="nav">
      <form>
          <input type="text" placeholder="Rechercher un Projet...">
          <input type="submit" value="Rechercher">
       </form>
      <Link to="/"><a href="App.svelte">ACCUEIL</a> </Link>
      <a href="about.html">PROPOS DE NOUS</a>
      <a href="about.html">MES INVESTISSEMENTS</a>
      <a href="image.html"><img src="images/126083.png" alt="Panier"></a>
  </div>
</header>
  

 
  <section class="about2">
    <main class="table">
        <section class="table__header">
            <h1>Catalogue de Produits</h1>
        </section>
        <section class="table__body">
            <table>
                       
                <thead>
                    <tr>
                        <th>Projet</th>
                        <th>Image</th>
                        <th>Prix de l'Action</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {#each projets as projet}
                        <tr>
                            <td>{projet.nom}</td>
                            <td><img src={projet.image} width="100" height="90" alt={projet.nom} /></td>
                            <td>${projet.prix}</td>
                            <td><button class="btn" on:click={() => acheterArticle(projet.id)}>Acheter des Actions</button></td>
                        </tr>
                    {/each}
                </tbody>
            </table>
        </section>
        <div class="message {messageColor}">
          {message}
      </div> 
    </main>
   

</section>
<Link to="/achat_client">
  <button class="add-project-btn"><img src="images/126083.png" alt="Panier" width="50"height="50"></button>
</Link>
    

  