///////////////////////////////////////////////////////////
//  triangle.h
//  Implementation of the Class CTriangle
//  Created on:      20-janv.-2026 10:08:10
//  Original author: Utilisateur
///////////////////////////////////////////////////////////

#if !defined(EA_27FAED55_15DC_44a5_A411_D9FB4F259080__INCLUDED_)
#define EA_27FAED55_15DC_44a5_A411_D9FB4F259080__INCLUDED_

#include "forme.h"

class CTriangle : public CForme
{

public:
	CTriangle();
	virtual ~CTriangle();

	CTriangle(string nom, int _hauteur, int _base);
	void afficher();
	double surface();

private:
	int base;
	int hauteur;

};
#endif // !defined(EA_27FAED55_15DC_44a5_A411_D9FB4F259080__INCLUDED_)
