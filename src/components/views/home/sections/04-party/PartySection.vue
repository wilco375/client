<template>
  <PageSection class="party-section" data-section="party" full role="form">
    <h2 class="party-section__heading">
      {{ $t('views.home.party.section.heading') }}
    </h2>
    <p class="party-section__introduction">
      {{ $t('views.home.party.section.instruction') }}
    </p>
    <ul
      :class="{
        'party-section__parties': true,
        'party-section__parties--logos': showLogos,
      }"
      role="list"
    >
      <li
        v-for="(party, index) in parties"
        :key="index"
        :class="{
          'party-section__party': true,
          'party-section__party--logos': showLogos,
        }"
      >
        <party :index="index" :show-logo="showLogos" :logo="party.logo" />
      </li>
    </ul>
    <div class="party-section__actions">
      <BaseButton
        theme="positive"
        left="check"
        size="large"
        :disabled="selectedParties.length < 2 || chosen"
        @click="$store.dispatch('parties/chose')"
      >
        {{ $t('views.home.party.section.proceed') }}
      </BaseButton>
    </div>
  </PageSection>
</template>

<script>
import PageSection from '@/components/elements/PageSection.vue';
import Party from '@/components/views/home/sections/04-party/Party.vue';

export default {
  name: 'PartySection',
  components: {
    PageSection,
    Party,
  },
  computed: {
    parties() {
      return this.$store.getters['parties/parties'];
    },
    selectedParties() {
      return this.$store.getters['parties/selectedParties'];
    },
    chosen() {
      return this.$store.getters['parties/chosen'];
    },
    showLogos() {
      return this.parties.some((party) => party.logo !== null);
    },
  },
};
</script>

<style lang="scss">
.party-section {
  border-top: 2px solid var(--theme-neutral-background);
}

.party-section__heading {
  color: var(--theme-primary-color);
}

.party-section__introduction {
  margin-bottom: 2.5em;
}

.party-section__parties {
  margin-bottom: 3em;
}

.party-section__actions {
  text-align: center;
}
</style>
