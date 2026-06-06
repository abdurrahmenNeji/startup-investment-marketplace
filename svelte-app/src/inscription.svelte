<script>
    import { Link , navigate} from "svelte-routing"; // Importez la fonction de navigation

    async function handleSubmit(event) {
        event.preventDefault();

        // Récupérer les données du formulaire
        const formData = new FormData(event.target);
        const token = 'f8d3a3e8643875a8f372a9e51716f12b28ff9752';
        const data = {
            nom: formData.get("last"),
            prenom: formData.get("first"),
            CIN: formData.get("cin"),
            email: formData.get("email"),
            pseudo: formData.get("username"),
            pwrd: formData.get("password"),
        };
        try {
            const response = await fetch('http://127.0.0.1:8000/capitalRisque/', {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    'Authorization': `Token ${token}`,
                },
                body: JSON.stringify(data),
            });

            if (response.ok) {
                const result = await response.json();
                alert("Données enregistrées avec succès !");
                console.log(result);

                // Redirection après succès
                navigate('/profileCapitaux');
            } else {
                const error = await response.json();
                alert("Erreur lors de l'enregistrement.");
                console.error(error);
            }
        } catch (error) {
            console.error("Erreur réseau :", error);
            alert("Une erreur réseau est survenue.");
        }
    }
</script>

<main>
    <section id="header-contact">
        <!-- Navbar -->
        <nav class="navbar">
            <div class="nav-items">
                <ul>
                    <li style="float:left;">
                        <a href="Index.html">
                            <img alt="" src="/images/start-up-branding-logo.png" width="150" height="80" />
                        </a>
                    </li>
                   
                    <li><Link to="/"><a href="App.svelte">ACCUEIL</a> </Link></li>
                    <li><a href="about.html">À PROPOS DE NOUS</a></li>
                    <li><a href="contact.html">CONTACT</a></li>
                </ul>
            </div>
        </nav>

        <!-- Title -->
        <div class="title">
            <h1 id="h1-title">CONTACT</h1>
        </div>
    </section>

    <!-- Contact Form -->
    <section>
        <div class="contactt">
            <div class="conty">
                <form on:submit|preventDefault={handleSubmit}>
                    <h3>Formulaire d'inscription</h3>
                    <div class="form-group">
                        <div class="form-contactt">
                            <label for="first">Prénom :</label><br />
                            <input type="text" id="first" name="first" required /><br />
                        </div>
                        <div class="form-contactt">
                            <label for="last">Nom :</label><br />
                            <input type="text" id="last" name="last" required /><br />
                        </div>
                        <div class="form-contactt">
                            <label for="cin">Numéro CIN (8 chiffres) :</label><br />
                            <input type="text" id="cin" name="cin" required /><br />
                        </div>
                        <div class="form-contactt">
                            <label for="email">Email :</label><br />
                            <input type="email" id="email" name="email" required /><br />
                        </div>
                        <div class="form-contactt">
                            <label for="username">Pseudo :</label><br />
                            <input type="text" id="username" name="username" required /><br />
                        </div>
                        <div class="form-contactt">
                            <label for="password">Mot de passe (au moins 8 caractères, finissant par $ ou #) :</label><br />
                            <input type="password" id="password" name="password"  /><br />
                        </div>
                    </div>
                    <div style="text-align:center;">
                        <button type="submit" class="myButton-title">Envoyer</button>
                    </div>
                </form>
            </div>
        </div>
    </section>
    
</main>
