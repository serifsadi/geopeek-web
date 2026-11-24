// Single source for release facts. Update on each release.
// Verified 2026-11-24 against GitHub Releases, the repo README and the Homebrew tap README.
export const SITE = {
  url: 'https://geopeek.app',
  name: 'GeoPeek',
  version: '0.4.1',
  released: '2026-11-23',
  dmgName: 'GeoPeek-0.4.1.dmg',
  dmgUrl: 'https://github.com/serifsadi/geopeek/releases/download/v0.4.1/GeoPeek-0.4.1.dmg',
  dmgSize: '2.8 MB', // 2,780,712 bytes
  releasesUrl: 'https://github.com/serifsadi/geopeek/releases',
  releaseNotesUrl: 'https://github.com/serifsadi/geopeek/releases/tag/v0.4.1',
  repoUrl: 'https://github.com/serifsadi/geopeek',
  issuesUrl: 'https://github.com/serifsadi/geopeek/issues',
  newIssueUrl: 'https://github.com/serifsadi/geopeek/issues/new',
  licenseUrl: 'https://github.com/serifsadi/geopeek/blob/main/LICENSE',
  changelogUrl: 'https://github.com/serifsadi/geopeek/blob/main/CHANGELOG.md',
  brew: 'brew install --cask serifsadi/geopeek/geopeek',
  brewTrust: 'brew trust --cask serifsadi/geopeek/geopeek',
  minMacOS: '15.0',
  author: 'Şerif Şadi Şenkule',
  authorUrl: 'https://serifsadi.dev',
} as const;
