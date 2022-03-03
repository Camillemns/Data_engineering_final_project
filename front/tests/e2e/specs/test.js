// https://docs.cypress.io/api/introduction/api.html

describe('My First Test', () => {
  it('Visits the app root url', () => {
    cy.visit('/')
    cy.request('POST', 'http://localhost:8000/get_toxicity', {
      text: 'this is bullshit'
    })

    cy.get('#result', { timeout: 10000 }).should('be.visible');

    cy.contains('#result', 'toxicity')
  })
})
