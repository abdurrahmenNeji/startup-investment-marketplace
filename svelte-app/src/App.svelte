<script>
  import { Router, Route, Link } from 'svelte-routing';  // Importation de svelte-routing
   import Achat_client from './achat_client.svelte'; // Composant profile
   import ProfileCapitaux from './profileCapitaux.svelte';
   import Inscription from './inscription.svelte';
   
   import './style.css';
   function openModal() {
       document.getElementById("myModal").style.display = "block";
     }
   
     function closeModal() {
       document.getElementById("myModal").style.display = "none";
     }
   
     function openModal2() {
       document.getElementById("myModal2").style.display = "block";
     }
   
     function closeModal2() {
       document.getElementById("myModal2").style.display = "none";
     }
   
 </script>
 
 <Router>
   <!-- Page d'accueil -->
   <Route path="/" let:params>
     <main>
        <!-- Section d'entête -->
     <section id="header-index">
       <!-- Navbar -->
       <nav class="navbar">
         <div class="nav-items">
           <ul>
             <li style="float:left;">
               <a href="Index.html">
                 <!-- svelte-ignore a11y-missing-attribute -->
                 <img src="images/start-up-branding-logo.png" width="150" height="80" />
               </a>
             </li>
             <li><a href="Index.html">ACCUEIL</a></li>
             <li><a href="about.html">À PROPOS DE NOUS</a></li>
             <div class="dropdown">
               <li>
                 <!-- svelte-ignore a11y-invalid-attribute -->
                 <a class="dropbtn" href="">S'INSCRIRE</a>
                 <div class="dropdown-content">
                   <!-- svelte-ignore a11y-missing-content -->
                   <a href="moment2.html"></a>
                   <a href="moment3.html">En tant que startuper</a>
                   <a href="moment4.html">En tant capital-risque</a>
                 </div>
               </li>
             </div>
             <li><a href="contact.html">CONTACT</a></li>
           </ul>
         </div>
       </nav>
       <video src="/images/PPP.mp4" muted loop autoplay></video>
       <div class="overplay"></div>
   
       <!-- Titre -->
       <div class="parag">
         <div class="infor">
           <h1>Opportunités d'Achat Exclusives</h1>
           <p>
             Découvrez les opportunités d'investissement dans les start-ups. Nous vous accompagnons dans la recherche de
             projets prometteurs et dans la création de partenariats fructueux. Ensemble, donnons vie à l'innovation et
             façonnons l'avenir.
           </p>
           <div>
             <a href="about.html">
               <button class="myButton-title"><span>EN SAVOIR PLUS</span></button>
             </a>
           </div>
         </div>
       </div>
     </section>
   
     <!-- Section espaces -->
     <section class="espaces">
       <div class="espaces2">
         <h5>Opportunités d'Achat Exclusives</h5>
         <h1>EXPLOREZ DE NOUVEAUX HORIZONS</h1>
       </div>
     </section>
   
     <!-- Section Pilates -->
     <section class="Pilates">
       <video autoplay muted loop id="myVideo" class="video-background">
         <source src="/images/kk.mp4" type="video/mp4" />
         Votre navigateur ne prend pas en charge la lecture vidéo HTML5.
       </video>
       <div class="cont-Pilates">
         <div class="row">
           <div class="col">
             <h1>A PROPOS DE NOUS</h1>
             <p>
               Découvrez comment vous pouvez contribuer à façonner l'avenir en investissant dans des start-ups
               innovantes. Ensemble, nous pouvons créer un monde meilleur.
             </p>
             <a href="about.html">
               <button class="mybutton-regime1">En savoir plus</button>
             </a>
           </div>
         </div>
       </div>
     </section>
     <section class="esp">
       <div class="espaces3">
           <h5 >Prêt à découvrir les opportunités d'investissement les plus prometteuses ?</h5>
           <h1>INSCRIVEZ-VOUS MAINTENANT</h1>
 
       </div>
   </section>
   
 
     
          <!-- Section Startups et Capital-risque -->
 <section class="belle-section">
  
   <!-- Bloc Capital-risque -->
   <div class="conteneur feuille">
     <div class="contenu">
       <h2>Espace Client</h2>
       <p>Découvrez et achetez des articles à fort potentiel de satisfaction.</p>
     
       <!-- Bouton pour rediriger vers le profil -->
       <button class="mybutton-regime1" style="height:50px;" on:click={openModal2}>S'inscrire</button>
       
     </div>
     <i class="fas fa-hand-holding-usd fa-3x logo"></i>
   </div>
 
  
 </section>
 <!-- Modale Capital-risque -->
 <!-- Modale Capital-risque -->
 <div id="myModal2" class="modal">
   <div class="modal-content">
     <!-- svelte-ignore a11y-click-events-have-key-events -->
     <span class="clos" on:click={closeModal2}>&times;</span>
     <h2>Connexion</h2>
     <form id="loginForm2" action="capitaux-risque.php" method="post">
       <label for="username2">Nom d'utilisateur:</label><br />
       <input type="text" id="username2" name="username" /><br />
       <label for="password2">Mot de passe:</label><br />
       <input type="password" id="password2" name="password" /><br /><br />
       <input type="submit" value="Se connecter" />
     </form>
     <div class="create-account">
       <p>Vous n'avez pas de compte ?</p>
       <Link to="/inscription" >
       <button >Créer un compte</button>
       </Link>
     </div>
   </div>
 </div>
 <!-- Modale Avis -->
 <div id="myModal" class="modal">
  <div class="modal-content">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <span class="clos" on:click={closeModal}>&times;</span>
    <h2>Connexion</h2>
    <form id="loginForm2" action="capitaux-risque.php" method="post">
      <label for="cin">CIN :</label><br />
      <input type="text" id="cin" name="username" /><br />
      <label for="avis">Avis:</label><br />
      <input type="password" id="avis" name="password" /><br /><br />
      <input type="submit" value="Envoyer" />
    </form>
    <div class="create-account">
      <p>Vous n'avez pas de compte ?</p>
      <Link to="/inscription" >
      <button >Créer un compte</button>
      </Link>
    </div>
  </div>
</div>

       
     <!-- Section Contact -->
     <section class="espaces">
       <div class="espaces1">
         <h5>RENCONTRONS-NOUS POUR RÉSOUDRE VOS PROBLÈMES</h5>
         <h1>CONTACTEZ-NOUS</h1>
       </div>
     </section>
     
   
     <section id="Contact-ind">
      <div class="contact-index-cont">
        <p id="contactMessage">EXPRIMEZ-VOUS ET FAITES PARTAGER VOTRE EXPÉRIENCE AVEC NOS PRODUITS.</p>
    
        <!-- Formulaire réactif -->
        <div class="contact-form">
          <label for="userName">Votre Nom :</label>
          <input
            type="text"
            id="userName"
            placeholder="Entrez votre nom"
            oninput="updateMessage(event)"
          />
    
          <label for="userReview">Votre Avis :</label>
          <input
            type="text"
            id="userReview"
            placeholder="Partagez votre avis"
          />
    
          <button class="mybutton-regime1" onclick="submitReview()">Soumettre</button>
        </div>
      </div>
    
      <video autoplay muted loop id="myVideo">
        <source src="/images/istockphoto-1334382252-640_adpp_is.mp4" type="video/mp4" />
        Your browser does not support HTML5 video.
      </video>
    </section>
    
    <script>
      // Fonction pour mettre à jour le message en fonction du nom
      function updateMessage(event) {
        const userName = event.target.value || "";
        const contactMessage = document.getElementById("contactMessage");
        contactMessage.innerHTML = `<span style="color: #ff5722;">${userName.toUpperCase()}</span>, FAITES PARTAGER VOTRE EXPÉRIENCE AVEC NOS PRODUITS.`;
    
        // Mise à jour du titre de la page
        document.title = `${userName} - Plateforme d'Achat en Ligne`;
      }
    
      // Fonction pour soumettre l'avis
      function submitReview() {
        const userName = document.getElementById("userName").value || "Anonyme";
        const userReview = document.getElementById("userReview").value || "Pas d'avis soumis";
        alert(`Merci ${userName} pour votre avis : "${userReview}"`);
        document.getElementById("userReview").value = ""; // Réinitialiser l'avis
      }
    </script>
    
    <style>
      .contact-form {
        display: flex;
        flex-direction: column;
        gap: 10px;
        align-items: center;
      }
    
      .contact-form label {
        font-size: 1em;
        color: white;
      }
    
      .contact-form input {
        padding: 10px;
        font-size: 1em;
        border: none;
        border-radius: 4px;
        width: 80%;
        max-width: 300px;
        background-color: rgba(255, 255, 255, 0.8);
        color: #333;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
      }
    
      .contact-form input:focus {
        outline: none;
        background-color: white;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
      }
    
      #contactMessage {
        font-size: 1.5em;
        font-weight: bold;
        margin-bottom: 15px;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
        text-align: center;
      }
    
      #contactMessage span {
        font-weight: bold;
        color: #ff5722; /* Couleur vive pour attirer l'attention */
      }
    
     
      
    </style>
    
         <!-- espace -->
            <!-- Advantages -->
 
     <section class="Advantages">
       <div class="adv-box">
           <i class="fas fa-chart-line fa-4x" style="color: #FF5733;"></i>
           <h3>Investissement dans des projets innovants</h3>
           <p>Investir dans des start-ups offre l'opportunité de soutenir des projets innovants et prometteurs. En échange de financement, les start-upers peuvent offrir des parts de leur entreprise, offrant ainsi un potentiel de rendement attractif aux investisseurs.</p>
       </div>
   
       <div class="adv-box">
           <i class="fas fa-hands-helping fa-4x" style="color: #FFC300;"></i>
           <h3>Participer à des projets philanthropiques</h3>
           <p>En investissant dans des start-ups, vous pouvez également contribuer à des projets philanthropiques. Certains entrepreneurs intègrent des aspects de responsabilité sociale dans leurs entreprises, ce qui permet de soutenir des causes humanitaires et sociales tout en investissant.</p>
       </div>
   
       <div class="adv-box">
           <i class="fas fa-globe fa-4x" style="color: #33FF77;"></i>
           <h3>Construire un avenir durable</h3>
           <p>L'investissement dans des start-ups offre la possibilité de participer à la construction d'un avenir durable. De nombreuses start-ups se concentrent sur des domaines tels que les énergies renouvelables, la santé, l'éducation et d'autres solutions innovantes pour résoudre les défis mondiaux.</p>
       </div>
   </section>
 
 
 
         <section class="espaces" style="height:400px;">
           <div class="espaces1">
               <img  alt="" class="logo2" src="/images/start-up-branding-logo.png" >
               <h5 >Explorez nos projets les plus prometteurs</h5>
               <h1>GALERIE DE PROJETS</h1>
           </div>
       </section>
    
     
   
     
 
     <!-- Galerie -->
     <section class="Galerie">
       <div class="box">
         <img src="/images/8f7a9b4a10e3c3de192736e43755e637.jpg" width="300" height="300" alt="" />
       </div>
       <div class="box">
         <img src="/images/image-finale.jpg" width="300" height="300" alt="" />
       </div>
       <div class="box">
         <img src="/images/jjj.jfif" width="300" height="300" alt="" />
       </div>
       <div class="box">
         <img src="/images/remus-startup.jpg" width="300" height="300" alt="" />
       </div>
     </section>
       <!-- Section équipe -->
     <section id="team">
       <div class="team-box">
        
       </div>
     </section>
     <div class="footer_bar">
       <a href=" " class="social-link">
           <i class="fab fa-facebook-f"></i>
           <span class="social-text">Facebook</span>
       </a>
       <a href=" " class="social-link">
           <i class="fab fa-instagram"></i>
           <span class="social-text">Instagram</span>
       </a>
       <a href=" " class="social-link">
           <i class="fab fa-twitter"></i>
           <span class="social-text">Twitter</span>
       </a>
       <a href=" " class="social-link">
           <i class="fab fa-whatsapp"></i>
           <span class="social-text">WhatsApp</span>
       </a>
       <a href="mailto:votre@email.com" class="social-link">
           <i class="fas fa-envelope"></i>
           <span class="social-text">Email</span>
       </a>
       <div class="footer_bar">
           <a href="Index.html">
               <img alt="" src="/images/start-up-branding-logo.png" width="150" height="50">
           </a>
           <p>
               Copyright © 2023 Tous droits réservés | site réalisé par Wissal Ghiryani
           </p>
       </div>
       
   </div>
   
 
     <!-- Footer -->
     <footer>
       <p>&copy; 2024 Investissements et Startups. Tous droits réservés.</p>
     </footer>
 
    
     </main>
   </Route>
   <!-- Route vers Profile -->
   <Route path="/achat_client">
     <Achat_client />
   </Route>
 
   <!-- Route vers le composant profileCapitaux -->
   <Route path="/profileCapitaux">
     <ProfileCapitaux />
   </Route>
    <!-- Route vers le composant inscription -->
    <Route path="/inscription">
     <Inscription />
   </Route>
   
 </Router>
 