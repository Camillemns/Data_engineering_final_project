import { shallowMount } from '@vue/test-utils'
import flushPromises from 'flush-promises'
import Toxicity from '@/components/Toxicity.vue'

const sleep = (ms : number) => new Promise(resolve => setTimeout(resolve, ms))

describe('Toxicity.vue', () => {
  it('component worked', async () => {
    const wrapper = shallowMount(Toxicity)

    await wrapper.find('#form textarea')
    await wrapper.find('#form button').trigger('click')
  })


  jest.mock('axios')
  jest.setTimeout(30000);

  it('fetches async when a button is clicked', async () => {
    const wrapper = shallowMount(Toxicity)
    await wrapper.find('#submit').trigger('click')
    await sleep(10000)
    await flushPromises()
    expect(wrapper.find('#result').text()).toMatch(/\b(?:toxicity|severe)\b/g)
  })
})
