///////////////////////////////////////////////////////////
//  carre.cpp
//  Implementation of the Class CCarre
//  Created on:      20-janv.-2026 10:11:05
//  Original author: Utilisateur
///////////////////////////////////////////////////////////

#include "carre.h"
using namespace std;

CCarre::CCarre(){
	cote = 3;
}



CCarre::~CCarre(){

}


CCarre::CCarre(int _cote){
	cote = _cote;
}


void CCarre::afficher(){
	CForme::afficher();
	cout << "Cote : " << cote << endl;
	cout << "Surface : " << surface() << endl;
}

double CCarre::surface(){
	surface = cote * cote;
	return 0;
}