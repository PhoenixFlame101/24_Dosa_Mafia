import React from 'react';
import {View, Text, StyleSheet} from 'react-native';

export default function App() {
  return (
    <View style={styles.root}>
      <View style={styles.group14}>
        <View style={styles.items}>
          <Text style={styles.apple}>
            Apple
          </Text>
        </View>
      </View>
      <View style={styles.group13}>
        <View style={styles.items}>
          <Text style={styles.banana}>
            Banana
          </Text>
        </View>
      </View>
      <View style={styles.group12}>
        <View style={styles.items}>
          <Text style={styles.carrot}>
            Carrot
          </Text>
        </View>
      </View>
      <View style={styles.group11}>
        <View style={styles.items}>
          <Text style={styles.potato}>
            Potato
          </Text>
        </View>
      </View>
      <View style={styles.group9}>
        <View style={styles.items}>
          <Text style={styles.cauliflower}>
            Cauliflower
          </Text>
        </View>
      </View>
      <View style={styles.group7}>
        <View style={styles.items}>
          <Text style={styles.tomato}>
            Tomato
          </Text>
        </View>
      </View>
      <View style={styles.group6}>
        <View style={styles.items}>
          <Text style={styles.onion}>
            Onion
          </Text>
        </View>
      </View>
      <View style={styles.items}>
        <Text style={styles.onion}>
          Onion
        </Text>
      </View>
      <View style={styles.items}>
        <Text style={styles.onion}>
          Onion
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  root: {
    backgroundColor: 'rgb(13, 13, 13)',
  },
  apple: {
    color: 'rgb(255, 255, 255)',
    fontSize: 16,
    fontWeight: '700',
    textAlign: 'left',
  },
  banana: {
    color: 'rgb(255, 255, 255)',
    fontSize: 16,
    fontWeight: '700',
    textAlign: 'left',
  },
  carrot: {
    color: 'rgb(255, 255, 255)',
    fontSize: 16,
    fontWeight: '700',
    textAlign: 'left',
  },
  potato: {
    color: 'rgb(255, 255, 255)',
    fontSize: 16,
    fontWeight: '700',
    textAlign: 'left',
  },
  cauliflower: {
    color: 'rgb(255, 255, 255)',
    fontSize: '',
    fontWeight: '700',
    textAlign: 'left',
  },
  tomato: {
    color: 'rgb(255, 255, 255)',
    fontSize: 16,
    fontWeight: '700',
    textAlign: 'left',
  },
  onion: {
    color: 'rgb(0, 0, 0)',
    fontSize: 16,
    fontWeight: '700',
    textAlign: 'left',
  },
});