///////////////////////////////////////////////////////////
//  rectangle.cpp
//  Implementation of the Class CRetangle
//  Created on:      20-janv.-2026 10:20:43
//  Original author: Utilisateur
///////////////////////////////////////////////////////////

#include "rectangle.h"
using namespace std;

CRectangle::CRectangle(){
	nom = "rectangle inconnu";
	largeur = 4;
	longueur = 2;
}



/**
 * constructeur prends le paramètre "nom" de la classe de base et les deux
 * paramètres "longueur" et "largeur" propres à la classe CRectangle
 */
CRectangle::CRectangle(string nom, int _largeur, int _longueur) {
	nom = nom;
	largeur = _largeur;
	longueur = _longueur;
}


CRectangle::~CRectangle(){

}


/**
 * affiche le nom, la longueur, la largeur et la surface du rectangle
 */
void CRectangle::afficher(){
	CForme::afficher();
	cout << "Longueur : " << longueur << endl;
	cout << "Largeur : " << largeur << endl;
	cout << "Surface : " << surface() << endl;
}



/**
 * retourne la surface du rectangle
 */
double CRectangle::surface(){
	surface = largeur * longueur;
	return 0;
}