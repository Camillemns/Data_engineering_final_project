// https://docs.cypress.io/api/introduction/api.html

describe('E2E Test', () => {
  it('is the app working correctly', () => {
    cy.visit('/')

    cy.get('textarea').type('this is bullshit')

    cy.get('#submit').click()

    cy.get('#result', { timeout: 10000 }).should('be.visible');

    cy.contains('#result', 'toxicity')
  })

  it('is the app working correctly 2', () => {
    cy.visit('/')

    cy.get('textarea').type('this is bullshit')

    cy.get('#submit').click()

    cy.get('#result', { timeout: 10000 }).should('be.visible');

    cy.contains('#result', 'toxicity')
  })
})
