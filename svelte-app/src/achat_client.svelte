<script>
    import { Link } from 'svelte-routing';
    import axios from 'axios'; // Importer axios

    let client_id = 1; // ID du client
    let achats = []; // Liste des achats effectués par le client
    let message = ''; // Message pour afficher le statut de l'opération
    let messageColor = ''; // Couleur du message (vert ou rouge)
    const token = 'f8d3a3e8643875a8f372a9e51716f12b28ff9752'; // Remplacez par le jeton généré

    // Fonction pour récupérer les achats effectués par le client
    const fetchAchats = async () => {
        try {
            const response = await axios.get(`http://127.0.0.1:8000/achats/client/${client_id}/`, {
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                },
            });

            console.log("Données API récupérées :", response.data); // Vérifie la structure ici
            achats = response.data;
            message = "Achats récupérés avec succès!";
            messageColor = 'green';
        } catch (error) {
            console.error("Erreur API :", error);
            if (error.response) {
                // Erreur provenant du serveur
                message = `Erreur: ${error.response.data.error || "Problème de récupération des achats"}`;
            } else if (error.request) {
                // Erreur de requête sans réponse
                message = "Erreur réseau. Impossible de récupérer les achats.";
            } else {
                // Autre erreur
                message = "Une erreur inconnue est survenue.";
            }
            messageColor = 'red';
        }
    };

    // Appeler la fonction fetchAchats au chargement du composant
    fetchAchats();
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

    .table__body::-webkit-scrollbar {
        width: 0.5rem;
        height: 0.5rem;
    }

    .table__body::-webkit-scrollbar-thumb {
        border-radius: .5rem;
        background-color: #0004;
        visibility: hidden;
    }

    .table__body:hover::-webkit-scrollbar-thumb {
        visibility: visible;
    }

    table {
        width: 100%;
        border-collapse: collapse;
    }

    td,
    th {
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
    <h1>Espace Achats Réalisés</h1>
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
            <h1>Achats du Client</h1>
        </section>
        <section class="table__body">
            <table>
                <thead>
                    <tr>
                        <th>Article</th>
                        <th>Description</th>
                        <th>Quantité</th>
                    </tr>
                </thead>
                <tbody>
                    {#each achats as achat}
                    <tr>
                        <td>{achat.article_nom || 'Nom non défini'}</td>
                        <td>{achat.article_description || 'Aucune description'}</td>
                        <td>{achat.quantite || 0}</td>
                    </tr>
                    {/each}
                </tbody>
            </table>
        </section>
        <!-- Affichage du message -->
        {#if message}
            <div class="message" style="color: {messageColor};">
                {message}
            </div>
        {/if}
    </main>
</section>

<Link to="/profileCapitaux">
    <button class="add-project-btn">+</button>
</Link>
