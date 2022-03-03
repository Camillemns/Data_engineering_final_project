// For authoring Nightwatch tests, see
// https://nightwatchjs.org/guide
const nock = require('nock')
const sinon = require('sinon')

nock('http://localhost:8000')
  .post('/get_toxicity')
  .reply(200, { result: { toxicity: 0.8 } });

module.exports = {
  'is form element present': browser => {
    browser
      .openHomepage()
      .assert.elementPresent('#form')
      .end()
  },

  'is form submission working': browser => {
    const server = sinon.fakeServer.create();
    server.respondWith("POST", "/get_toxicity", [
      200,
      { "Content-Type": "application/json" },
      '[{ "id": 12, "comment": "Hey there" }]',
    ]);

    browser
      .openHomepage()
      .assert.elementPresent('#form')
      .setValue('textarea', 'this is bullshit')
      .click('button[type=submit]')
      .waitForElementVisible('#result', 1000000)
      .assert.containsText('#result', 'toxicity')
      .end()
  }
}
