///////////////////////////////////////////////////////////
//  triangle.cpp
//  Implementation of the Class CTriangle
//  Created on:      20-janv.-2026 10:08:10
//  Original author: Utilisateur
///////////////////////////////////////////////////////////

#include "triangle.h"
using namespace std;

CTriangle::CTriangle(){
	nom = "triangle inconnu";
	hauteur = 3;
	base = 4;
}



CTriangle::~CTriangle(){

}


CTriangle::CTriangle(string nom, int _hauteur, int _base){
	nom = nom;
	hauteur = _hauteur;
	base = _base;
}


void CTriangle::afficher(){
	CForme::afficher();
	cout << "Hauteur : " << hauteur << endl;
	cout << "Base : " << base << endl;
	cout << "Surface : " << surface() << endl;
}


double CTriangle::surface(){
	surface = (base * hauteur) / 2;
	return 0;
}