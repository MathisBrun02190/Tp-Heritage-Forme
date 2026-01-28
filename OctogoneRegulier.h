///////////////////////////////////////////////////////////
//  OctogoneRegulier.h
//  Implementation of the Class OctogoneRegulier
//  Created on:      20-janv.-2026 10:20:48
//  Original author: Utilisateur
///////////////////////////////////////////////////////////

#if !defined(EA_F4AA348A_CB84_4bda_BB01_CEB429BA389A__INCLUDED_)
#define EA_F4AA348A_CB84_4bda_BB01_CEB429BA389A__INCLUDED_

#include "forme.h"

class COctogoneRegulier : public CForme
{

public:
	COctogoneRegulier();
	virtual ~COctogoneRegulier();

	void afficher();
	COctogoneRegulier(string _nom, int _cote);
	double surface();

private:
	int cote;

};
#endif // !defined(EA_F4AA348A_CB84_4bda_BB01_CEB429BA389A__INCLUDED_)
