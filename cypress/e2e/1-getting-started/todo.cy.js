/// <reference types="cypress" />


describe('Tests des valeurs', () => {
  it('Accès au tableau de bord', () => {
    cy.visit('http://localhost:8501')
  })

  it ("Saisie de la surface de la maison", () => {
    cy.get('input').eq(0).clear().type("100.{enter}")
    })

  it ("Saisie du nombre de chambres", () => {
    cy.get('input').eq(1).clear().type("3.{enter}")
    })

  it ("Présence d'un jardin ou non", () => {
    cy.get('input').eq(2).clear().type("0.{enter}")
    })

  it ("Vérification que le prix de la maison n'est pas négatif", () => {
    cy.get('p').should('not.contain','-')
    })

  it("Vérification du prix de la maison", () => {
    cy.get('p').then((valeur) => {
      console.log(valeur)
      "console.log( 'PRIX :', valeur[0].innerText.substr(27))"
      var prix_maison = valeur[0].innerText.substr(27)
      cy.log("Respect du prix minimum (5 000)", prix_maison > 5000)
      cy.log("Respect du prix maximum (170 000)", prix_maison < 170000)
      })
    })
})




