///////////////////////////////////////////////////////////
//  carre.h
//  Implementation of the Class CCarre
//  Created on:      20-janv.-2026 10:11:05
//  Original author: Utilisateur
///////////////////////////////////////////////////////////

#if !defined(EA_CAB04089_B088_4860_A714_D5B6EA6C5D52__INCLUDED_)
#define EA_CAB04089_B088_4860_A714_D5B6EA6C5D52__INCLUDED_

#include "rectangle.h"

class CCarre : public CRectangle
{

public:
	CCarre();
	virtual ~CCarre();

	CCarre(int _cote);
	void afficher();
	double surface();

private:
	int cote;

};
#endif // !defined(EA_CAB04089_B088_4860_A714_D5B6EA6C5D52__INCLUDED_)
