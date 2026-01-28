///////////////////////////////////////////////////////////
//  forme.h
//  Implementation of the Class CForme
//  Created on:      20-janv.-2026 10:20:36
//  Original author: Utilisateur
///////////////////////////////////////////////////////////

#if !defined(EA_C6A867D6_1E90_4f6f_9136_67255E5B0D6C__INCLUDED_)
#define EA_C6A867D6_1E90_4f6f_9136_67255E5B0D6C__INCLUDED_

#include <string>
using namespace std;

class CForme
{

public:
	CForme();
	~CForme();

	CForme(string _nom);
	void afficher();
	/**
	* la méthode surface est déjà en méthode normale 
	*/
	double surface();

private:
	/**
	 * nom de la forme pour l'identifier. Ce nom sera affiché dans la méthode affiche()
	 */
	string nom;

};
#endif // !defined(EA_C6A867D6_1E90_4f6f_9136_67255E5B0D6C__INCLUDED_)
