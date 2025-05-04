<?php
// Configuration des paramètres de la base de données
$servername = "localhost";
$username = "pdy10996_admin";
$password = "Eeemixam123%";
$dbname = "pdy10996_abonnements";

// Connexion à la base de données
$conn = new mysqli($servername, $username, $password, $dbname);

// Vérifiez la connexion
if ($conn->connect_error) {
    die("Échec de la connexion à la base de données: " . $conn->connect_error);
}

// Vérifiez si le formulaire a été soumis
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Obtenez l'email du formulaire
    $email = $conn->real_escape_string(trim($_POST['email']));

    // Vérifiez si l'email est déjà dans la base de données
    $check_sql = "SELECT email FROM abonnements WHERE email = '$email'";
    $check_result = $conn->query($check_sql);

    if ($check_result->num_rows == 0) {
        // Insérez l'email dans la base de données
        $sql = "INSERT INTO abonnements (email) VALUES ('$email')";

        if ($conn->query($sql) === TRUE) {
            echo "Merci de vous être abonné. Votre email a été ajouté avec succès.";
        } else {
            echo "Erreur: " . $sql . "<br>" . $conn->error;
        }
    } else {
        echo "Cet email est déjà inscrit.";
    }
}

// Fermer la connexion à la base de données
$conn->close();
?>
